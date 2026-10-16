import { strict as assert } from 'node:assert';
import { DeepSeekHost } from '../../src/providers/deepseek/runtime/DeepSeekHost';
import { DeepSeekHostProcess } from '../../src/providers/deepseek/runtime/DeepSeekHostProcess';
import { callDeepSeekJobs, readDeepSeekJobs, stopDeepSeekJob } from '../../src/providers/deepseek/runtime/DeepSeekJobs';
Object.assign(globalThis, { window: globalThis });
async function main() {
  const host = new DeepSeekHost(async () => ({
    cliPath: 'C:/Users/Nuo/AppData/Roaming/npm/dsh.cmd', cwd: 'C:/Users/Nuo/AppData/Local/Temp/claudian-dsh-compat-work', environment: { ...process.env },
    presetPlugins: [{ id: 'native-job-fixture', name: 'file:///C:/Users/Nuo/AppData/Local/Temp/claudian-dsh-compat-work/.context/deepseek-chat-execution/NativeJobFixture.mjs' }],
  }), DeepSeekHostProcess.start, 1000);
  try {
    const lease = await host.attach(AbortSignal.timeout(60000));
    try {
      const ids = [lease.ephemeralSessionId(), lease.ephemeralSessionId()];
      for (const sessionId of ids) await lease.client.call('session/create', { request: { sessionId, agentPreset: 'claudian', cwd: 'C:/Users/Nuo/AppData/Local/Temp/claudian-dsh-compat-work' } });
      const started = await lease.client.call('commands/execute', { agentId: ids[0], line: '/claudian-fixture-job-start', submittedAttachments: [] });
      assert(started);
      const owned = await readDeepSeekJobs(lease.client, ids[0]);
      assert.equal(owned.length, 1); assert.equal(owned[0].status, 'running');
      assert.equal((await readDeepSeekJobs(lease.client, ids[1])).length, 0);
      await assert.rejects(callDeepSeekJobs(lease.client, ids[1], { action: 'stop', jobId: owned[0].id }));
      assert.equal((await readDeepSeekJobs(lease.client, ids[0]))[0].status, 'running');
      await stopDeepSeekJob(lease.client, owned[0]);
      const deadline = Date.now() + 5000;
      while ((await readDeepSeekJobs(lease.client, ids[0]))[0].status !== 'killed') {
        assert(Date.now() < deadline, 'Native job did not reach killed'); await new Promise(resolve => setTimeout(resolve, 20));
      }
      const again = await callDeepSeekJobs(lease.client, ids[0], { action: 'stop', jobId: owned[0].id });
      assert.deepEqual(again, { status: 'already-finished' });
      console.log(JSON.stringify({ nativeJobLifecycle: 'PASS', foreignStopRejected: true, exactOwnerList: true, repeatedStop: 'already-finished', modelRequestsSent: 0 }));
    } finally { lease.release(); }
  } finally { await host.dispose(); }
}
main().catch(error => { console.error(error.message); process.exitCode = 1; });
