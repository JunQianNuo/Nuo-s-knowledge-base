import { NativePeer } from '@test/helpers/deepseek/NativePeer';

import { readDeepSeekProjection } from '@/providers/deepseek/history/DeepSeekJournal';

it('cold reads the current list projection without using removed projection RPCs or activating a session', async () => {
  const peer = new NativePeer(); await peer.open();
  try {
    peer.onCall = method => {
      if (method !== 'session/list') throw new Error(`Removed or activating endpoint: ${method}`);
      return { items: [{ sessionId: 'cold', running: false, projections: { asOfSeq: 7, values: { agentPreset: 'claudian' } } }] };
    };
    await expect(readDeepSeekProjection(peer.client, 'cold')).resolves.toEqual({ asOfSeq: 7, values: { agentPreset: 'claudian' } });
    await expect(readDeepSeekProjection(peer.client, 'absent')).rejects.toMatchObject({ code: 'session/missing' });
    peer.onCall = () => ({ items: [{ sessionId: 'cold', running: false }] });
    await expect(readDeepSeekProjection(peer.client, 'cold')).rejects.not.toMatchObject({ code: 'session/missing' });
    expect([...peer.streams.values()].some(stream => stream.endpoint === 'session/follow')).toBe(false);
  } finally { await peer.close(); }
});
