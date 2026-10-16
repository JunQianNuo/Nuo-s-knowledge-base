import { NativePeer, rootFollow } from '@test/helpers/deepseek/NativePeer';
import { testDate } from '@test/helpers/testClock';

import { DeepSeekSessionObserver } from '@/providers/deepseek/execution/DeepSeekSessionObserver';
import { DeepSeekRoster } from '@/providers/deepseek/runtime/DeepSeekRoster';

let peer: NativePeer;
let roster: DeepSeekRoster;
let observer: DeepSeekSessionObserver | undefined;
let jobs: Map<string, unknown[]>;
let readJobs: (id: string) => unknown[] | Promise<unknown[]>;
const row = (sessionId: string, extra = {}) => ({ sessionId, running: false, agentAvailable: true, ...extra });

beforeEach(async () => {
  peer = new NativePeer(); await peer.open();
  roster = new DeepSeekRoster(peer.client, error => { throw error; });
  jobs = new Map(); readJobs = id => jobs.get(id) ?? [];
});
afterEach(async () => { observer?.dispose(); observer = undefined; roster.dispose(); await peer.close(); });

function observe(rootId: string): DeepSeekSessionObserver {
  roster.claim(rootId, () => {});
  return new DeepSeekSessionObserver(peer.client, roster, rootId, () => {}, error => { throw error; });
}

function jobCall(method: string, args: Record<string, any>): unknown {
  if (method === 'commands/list') return [{ name: 'claudian-internal-jobs-fixture' }];
  if (method === 'commands/execute') return Promise.resolve(readJobs(args.agentId)).then(value => ({ result: { kind: 'success', text: JSON.stringify(value) } }));
  throw new Error(`Unexpected ${method}`);
}

it('becomes ready from current native control jobs without opening the removed job list endpoint', async () => {
  const failures: Error[] = [];
  jobs.set('root', [{ id: 'native-job', ownerSession: 'root', status: 'running' }]);
  peer.onCall = (method, args) => method === 'session/list' ? ({ items: [{ sessionId: 'root', running: false }] }) : jobCall(method, args);
  peer.onOpen = (endpoint, _args, send, fail) => {
    if (endpoint === 'session/control') send({ type: 'baseline', value: {
      queues: { root: [] },
      jobs: { root: [{ id: 'native-job', status: 'running' }] },
      projections: { root: { values: {} } },
    } });
    if (endpoint === 'session/follow') send({ type: 'snapshot', cursor: -1, records: [] });
    if (endpoint === 'job/list') fail!({ code: 'gateway/endpoint-not-found', message: 'job/list has no active Remote export' });
  };
  await roster.start();
  roster.claim('root', () => {});
  observer = new DeepSeekSessionObserver(peer.client, roster, 'root', () => {}, error => failures.push(error));
  await expect(observer.start()).resolves.toBeUndefined();
  expect(observer.isReady()).toBe(true);
  expect(observer.hasWork()).toBe(true);
  expect(observer.ownedJobs()).toEqual([{ id: 'native-job', owner: 'root', status: 'running' }]);
  expect(failures).toEqual([]);
  jobs.set('root', []);
  peer.send('session/control', { type: 'jobs', sessionId: 'root', jobs: [] });
  await until(() => !observer!.hasWork());
});

it('keeps status changes during roster loading and waits for descendant job baselines', async () => {
  let releaseRoster!: (value: unknown) => void;
  let childJobs!: (value: unknown[]) => void;
  readJobs = id => id === 'child' ? new Promise(resolve => { childJobs = resolve; }) : [];
  peer.onCall = (method, args) => method === 'session/list' ? new Promise(resolve => { releaseRoster = resolve; }) : jobCall(method, args);
  peer.onOpen = (endpoint, args, send) => {
    if (endpoint === 'session/control') send({ type: 'baseline', value: { queues: { root: [], child: [] }, jobs: { root: [], child: [] }, projections: { root: { values: { subagentCatalog: [{ id: 'child', mode: 'one-shot' }, { id: 'cold', mode: 'continuable' }] } }, child: { values: { subagent: { mode: 'one-shot', seq: 1 } } } } } });
    if (endpoint === 'session/follow') send({ type: 'snapshot', cursor: 0, records: [], projections: { asOfSeq: 0, values: {} } });
    if (endpoint === 'job/list') {
      if (args.request.sessionId === 'child') childJobs = send;
      else send({ type: 'rows', jobs: [{ id: 'unowned', status: 'running' }] });
    }
  };
  const listing = roster.start();
  observer = observe('root');
  const ready = observer.start();
  await until(() => !!releaseRoster);
  peer.send('$events', { type: 'emit', event: 'api-session/status', args: ['root', true] });
  releaseRoster({ items: [row('root', { parentSessionId: 'source' }), row('child', { parentSessionId: 'root', origin: 'subagent' }), row('cold', { parentSessionId: 'root', origin: 'subagent', agentAvailable: false }), row('sibling')] });
  await listing;
  await until(() => !!childJobs);
  expect(observer.hasWork()).toBe(true);
  jobs.set('child', [{ id: 'child-job', ownerSession: 'child', status: 'running' }]);
  readJobs = id => jobs.get(id) ?? [];
  childJobs(jobs.get('child')!);
  await ready;
  expect(observer.permissionBoundaryAvailable()).toBe(false);
  peer.send('$events', { type: 'emit', event: 'api-session/status', args: ['root', false] });
  await until(() => observer!.permissionBoundaryAvailable());
  expect(observer.hasWork()).toBe(true);
  expect(observer.ownedJobs()).toEqual([{ id: 'child-job', owner: 'child', status: 'running' }]);
  expect([...peer.streams.values()].filter(s => s.endpoint === 'session/follow').map(s => s.args.request.address)).toEqual(expect.arrayContaining([
    { kind: 'session', sessionId: 'root' }, { kind: 'subagent', childSessionId: 'child', parentSessionId: 'root', mode: 'one-shot' },
  ]));
  expect([...peer.streams.values()].some(s => JSON.stringify(s.args).includes('cold'))).toBe(false);
  jobs.set('child', []);
  peer.send('session/control', { type: 'jobs', sessionId: 'child', jobs: [] });
  await until(() => !observer!.hasWork());
});

it('follows a native child only after its durable identity, and keeps it busy until then', async () => {
  const rejected: unknown[] = [];
  const errors: Error[] = [];
  peer.onCall = (method, args) => method === 'session/list' ? ({ items: [row('root'), row('child', { parentSessionId: 'root', origin: 'subagent', running: true })] }) : jobCall(method, args);
  peer.onOpen = (endpoint, args, send, fail) => {
    if (endpoint === 'session/control') send({ type: 'baseline', value: { queues: { root: [], child: [] }, jobs: { root: [], child: [] }, projections: { root: { values: { subagentCatalog: [{ id: 'child', mode: 'one-shot', label: 'task' }] } }, child: { values: { subagent: null } } } } });
    if (endpoint === 'session/follow') {
      // rc.2 validates the child's durable descriptor identity before following.
      if (args.request.address.kind === 'subagent' && !(roster.projection('child')?.subagent)) {
        rejected.push(args.request.address); fail!({ code: 'subagent/catalog-diagnostic', message: 'subagent descriptor is corrupt' }); return;
      }
      send({ type: 'snapshot', cursor: 0, records: [], projections: { asOfSeq: 0, values: {} } });
    }
    if (endpoint === 'job/list') send({ type: 'rows', jobs: [] });
  };
  await roster.start();
  roster.claim('root', () => {});
  observer = new DeepSeekSessionObserver(peer.client, roster, 'root', () => {}, error => errors.push(error));
  const ready = observer.start();
  // The first reconcile already ran; the peer has handled its opens and the client their replies.
  await streamBarrier();
  expect(rejected).toEqual([]);
  expect(errors).toEqual([]);
  expect(observer.hasWork()).toBe(true);
  peer.send('session/control', { type: 'projection', sessionId: 'child', key: 'subagent', value: { mode: 'one-shot', label: 'task', seq: 3 }, seq: 3 });
  await ready;
  expect([...peer.streams.values()].filter(s => s.endpoint === 'session/follow').map(s => s.args.request.address)).toContainEqual(
    { kind: 'subagent', childSessionId: 'child', parentSessionId: 'root', mode: 'one-shot' });
  expect(rejected).toEqual([]);
  expect(errors).toEqual([]);
});

it('closes the permission boundary while a native tool call is unresolved', async () => {
  peer.onCall = (method, args) => method === 'session/list' ? ({ items: [row('root')] }) : jobCall(method, args);
  peer.onOpen = (endpoint, _args, send) => {
    if (endpoint === 'session/control') send({ type: 'baseline', value: { queues: { root: [] }, jobs: { root: [] }, projections: {} } });
    if (endpoint === 'session/follow') send({ type: 'snapshot', cursor: 0, records: [], projections: { asOfSeq: 0, values: {} } });
    if (endpoint === 'job/list') send({ type: 'rows', jobs: [] });
  };
  await roster.start();
  observer = observe('root');
  await observer.start();
  expect(observer.permissionBoundaryAvailable()).toBe(true);
  const event = (type: string, data: unknown) => peer.send('session/follow', { type: 'event', event: { type, seq: 1, time: testDate().getTime(), data } }, rootFollow('root'));
  // No turn boundary is followed, so only the unresolved call can hold the boundary.
  event('tool/call', { callId: 'bash-1', name: 'bash', arguments: '{}' });
  await until(() => observer!.hasWork());
  expect(observer.permissionBoundaryAvailable()).toBe(false);
  event('tool/result', { message: { toolCallId: 'bash-1' } });
  await until(() => observer!.permissionBoundaryAvailable());
  expect(observer.hasWork()).toBe(false);
});

it('projects restored queues and makes disconnect unknown until all baselines return', async () => {
  peer.onCall = (method, args) => method === 'session/list' ? ({ items: [row('root')] }) : jobCall(method, args);
  peer.onOpen = (endpoint, _args, send) => {
    if (endpoint === 'session/control') send({ type: 'baseline', value: { queues: { root: [{ id: 'queued', placement: 'queued', rpcId: 'old', message: { id: 'queued', content: [{ type: 'text', text: 'old task' }] } }] }, jobs: { root: [] }, projections: {} } });
    if (endpoint === 'session/follow') send({ type: 'snapshot', cursor: 4, records: [], projections: { asOfSeq: 4, values: {} } });
    if (endpoint === 'job/list') send({ type: 'rows', jobs: [] });
  };
  await roster.start();
  observer = observe('root');
  await observer.start();
  expect(observer.queuedItems('root')).toMatchObject([{ id: 'queued', source: { rpcId: 'old' } }]);
  expect(observer.hasWork()).toBe(true);
  roster.reset();
  expect(observer.permissionBoundaryAvailable()).toBe(false);
  expect(observer.hasWork()).toBe(true);
});

/** Resolves once the peer handled every stream the client opened before it, and the client received their replies. */
async function streamBarrier(): Promise<void> {
  let replied = false;
  const off = peer.client.subscribe('session/control', {}, () => { replied = true; }, () => { replied = true; });
  try { await until(() => replied); } finally { off(); }
}

async function until(predicate: () => boolean): Promise<void> {
  const deadline = Date.now() + 2000;
  while (!predicate()) {
    if (Date.now() > deadline) throw new Error('Native fixture condition timed out.');
    await new Promise(resolve => setTimeout(resolve, 5));
  }
}
