import { NativePeer } from '@test/helpers/deepseek/NativePeer';

import { DeepSeekRoster } from '@/providers/deepseek/runtime/DeepSeekRoster';

let peer: NativePeer;
let roster: DeepSeekRoster;
const row = (sessionId: string, extra = {}) => ({ sessionId, running: false, agentAvailable: true, ...extra });

beforeEach(async () => {
  peer = new NativePeer(); await peer.open();
  roster = new DeepSeekRoster(peer.client, error => { throw error; });
});
afterEach(async () => { roster.dispose(); await peer.close(); });

it('routes subagent work to its claimed root and keeps forks, which name their source as native parent, independent', async () => {
  const child = (parentSessionId: string) => ({ parentSessionId, origin: 'subagent' });
  peer.onCall = () => ({ items: [row('source'), row('fork', { parentSessionId: 'source' }), row('fork-child', child('fork')), row('source-child', child('source'))] });
  peer.onOpen = (endpoint, _args, send) => {
    if (endpoint === 'session/control') send({ type: 'baseline', value: { projections: {} } });
  };
  const sourceQuestions: unknown[] = []; const forkQuestions: unknown[] = [];
  roster.claim('source', event => sourceQuestions.push(event.eventId));
  await roster.start();
  // A closed fork stays loaded natively; its work must not become the source's.
  peer.send('$events', { type: 'waterfall', eventId: 'fork-question', event: 'user-questions/request', agentId: 'fork-child', request: {} });
  peer.send('$events', { type: 'waterfall', eventId: 'source-own', event: 'user-questions/request', agentId: 'source-child', request: {} });
  await until(() => sourceQuestions.length === 1);
  expect(sourceQuestions).toEqual(['source-own']);
  expect(roster.owner('fork')).toBeUndefined();
  expect(roster.owner('fork-child')).toBeUndefined();
  // Reopening the fork claims it and receives the interaction that was waiting for an owner.
  roster.claim('fork', event => forkQuestions.push(event.eventId));
  expect(forkQuestions).toEqual(['fork-question']);
  expect(roster.owner('fork-child')).toBe('fork');
  expect(sourceQuestions).toEqual(['source-own']);
  expect(() => roster.claim('fork', () => {})).toThrow(/already open/);
});

async function until(predicate: () => boolean): Promise<void> {
  const deadline = Date.now() + 2000;
  while (!predicate()) {
    if (Date.now() > deadline) throw new Error('Native fixture condition timed out.');
    await new Promise(resolve => setTimeout(resolve, 5));
  }
}

// New summaries omit agentAvailable. Cold rows stay inactive; live control evidence and legacy flags retain their meaning.
it('starts from mixed legacy and current session summaries and accepts current added events', async () => {
  peer.onCall = () => ({ items: [
    { sessionId: 'current', running: false, blank: true, cwd: '/vault' },
    { sessionId: 'current-idle-live', running: false, blank: false, cwd: '/vault' },
    { sessionId: 'legacy-unavailable', running: true, agentAvailable: false },
  ] });
  peer.onOpen = (endpoint, _args, send) => {
    if (endpoint === 'session/control') send({ type: 'baseline', value: { projections: { 'current-idle-live': { values: {} }, 'legacy-unavailable': { values: {} } } } });
  };
  await roster.start();
  await until(() => roster.ready);
  expect(roster.row('current')).toEqual({ id: 'current', available: false, running: false });
  expect(roster.row('current-idle-live')).toEqual({ id: 'current-idle-live', available: true, running: false });
  expect(roster.row('legacy-unavailable')).toEqual({ id: 'legacy-unavailable', available: false, running: true });
  peer.send('$events', { event: 'api-session/added', args: [{ sessionId: 'current-added', running: true, blank: false, cwd: '/vault' }] });
  await until(() => !!roster.row('current-added'));
  expect(roster.row('current-added')).toEqual({ id: 'current-added', available: true, running: true });
  expect(Array.from(roster.allRows())).toEqual([
    { id: 'current', available: false, running: false },
    { id: 'current-idle-live', available: true, running: false },
    { id: 'legacy-unavailable', available: false, running: true },
    { id: 'current-added', available: true, running: true },
  ]);
  peer.send('$events', { event: 'api-session/removed', args: ['current-idle-live'] });
  await until(() => roster.row('current-idle-live')?.available === false);
  expect(roster.row('current-idle-live')).toEqual({ id: 'current-idle-live', available: false, running: false });
  peer.send('$events', { event: 'api-session/status', args: ['current-idle-live', true] });
  peer.send('session/control', { type: 'projection', sessionId: 'current-idle-live', key: 'late', value: true });
  await until(() => roster.projection('current-idle-live')?.late === true);
  expect(roster.row('current-idle-live')).toEqual({ id: 'current-idle-live', available: false, running: true });
  peer.send('session/control', { type: 'projection', sessionId: 'current', key: 'live', value: true });
  await until(() => roster.row('current')?.available === true);
});

it.each([
  { sessionId: 'invalid', running: false, agentAvailable: 'true' },
  { sessionId: 'invalid', running: false, agentAvailable: null },
  { sessionId: 'invalid', running: 'false' },
  { running: false },
])('rejects malformed session fields instead of treating them as available', async value => {
  peer.onCall = () => ({ items: [value] });
  peer.onOpen = (endpoint, _args, send) => {
    if (endpoint === 'session/control') send({ type: 'baseline', value: { projections: {} } });
  };
  await expect(roster.start()).rejects.toThrow('Malformed DeepSeek session row.');
});

it('keeps its control subscription alive across current native queue and job updates', async () => {
  const failures: Error[] = [];
  roster.dispose();
  roster = new DeepSeekRoster(peer.client, error => failures.push(error));
  peer.onCall = () => ({ items: [{ sessionId: 'root', running: false }] });
  peer.onOpen = (endpoint, _args, send) => {
    if (endpoint === 'session/control') send({ type: 'baseline', value: {
      queues: { root: [] }, jobs: { root: [] },
      projections: { root: { values: {} } },
    } });
  };
  await roster.start();
  await until(() => roster.ready);
  peer.send('session/control', { type: 'jobs', sessionId: 'root', jobs: [{ id: 'job-1', status: 'running' }] });
  peer.send('session/control', { type: 'queue', sessionId: 'root', items: [{ id: 'queue-1', placement: 'queued', rpcId: 'request-1', message: { id: 'queue-1', content: [] } }] });
  peer.send('session/control', { type: 'projection', sessionId: 'root', key: 'deliveryMarker', value: true });
  await until(() => failures.length > 0 || roster.projection('root')?.deliveryMarker === true);
  expect(failures).toEqual([]);
  expect(roster.projection('root')?.deliveryMarker).toBe(true);
  expect(roster.control('root')?.queue).toEqual([{ id: 'queue-1', content: [], source: { kind: 'user', rpcId: 'request-1' } }]);
});

it('ignores a job read failure from a control generation that was reset', async () => {
  const failures: Error[] = [];
  roster.dispose(); roster = new DeepSeekRoster(peer.client, error => failures.push(error));
  peer.onCall = method => method === 'commands/list' ? [{ name: 'claudian-internal-jobs-fixture' }] : { items: [{ sessionId: 'root', running: false }] };
  peer.onOpen = (endpoint, _args, send) => {
    if (endpoint === 'session/control') send({ type: 'baseline', value: { queues: { root: [] }, jobs: { root: [] }, projections: {} } });
  };
  let rejectRead!: (error: Error) => void;
  const pending = new Promise<unknown>((_resolve, reject) => { rejectRead = reject; });
  const originalCall = peer.client.call.bind(peer.client);
  const calls = jest.spyOn(peer.client, 'call').mockImplementation((method, args, options) => method === 'commands/execute' ? pending : originalCall(method, args, options));
  await roster.start(); await until(() => roster.ready);
  const stop = roster.watchJobs('root');
  await until(() => calls.mock.calls.some(([method]) => method === 'commands/execute'));
  roster.reset(); await roster.start(); await until(() => roster.ready);
  rejectRead(new Error('Old transport ended'));
  await new Promise(resolve => setImmediate(resolve));
  expect(failures).toEqual([]);
  expect(roster.ready).toBe(true);
  stop(); calls.mockRestore();
});
