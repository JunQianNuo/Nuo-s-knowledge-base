import { execFile } from 'node:child_process';
import { promisify } from 'node:util';

import { readLaunchPresets } from '@test/helpers/deepseek/LaunchPresets';

import { prepareDeepSeekLaunchArtifacts } from '@/providers/deepseek/runtime/DeepSeekLaunchArtifacts';

it('packages a scoped job command that rejects foreign and ownerless work and distinguishes stop admission', async () => {
  const artifacts = await prepareDeepSeekLaunchArtifacts();
  try {
    const rows = (await readLaunchPresets(artifacts.patchPath)).claudian;
    const bridge = rows.find(row => row.id === 'claudian-job-control');
    expect(bridge).toBeDefined();
    const { stdout } = await promisify(execFile)(process.execPath, ['--input-type=module', '-e', `
      const plugin = await import(process.argv[1]);
      const config = JSON.parse(process.argv[2]);
      let command; const killed = [];
      const jobs = [
        { id: 'own', ownerSession: 'root', status: 'running' },
        { id: 'other', ownerSession: 'other-root', status: 'running' },
        { id: 'global', status: 'running' },
      ];
      plugin.apply({ commands: { register: value => { command = value; } }, jobs: {
        list: () => jobs,
        get: id => { const job = jobs.find(job => job.id === id); if (!job) throw Error('unknown job'); return job; },
        kill: (id, caller) => { killed.push({ id, caller: caller.id }); return 'requested'; },
      } }, config);
      const invoke = async value => command.handler({ agent: { id: 'root' }, rawInput: value, signal: new AbortController().signal });
      const listed = await invoke(JSON.stringify({ action: 'list' }));
      const stopped = await invoke(JSON.stringify({ action: 'stop', jobId: 'own' }));
      const rejected = [];
      for (const value of ['{', JSON.stringify({ action: 'stop', jobId: 'other' }), JSON.stringify({ action: 'stop', jobId: 'global' }), JSON.stringify({ action: 'stop', jobId: 'missing' }), JSON.stringify({ action: 'eval' }), JSON.stringify({ action: 'list', agentId: 'other-root' })]) {
        try { const result = await invoke(value); rejected.push(result.kind === 'error'); } catch { rejected.push(true); }
      }
      const abort = new AbortController(); abort.abort();
      try { await command.handler({ agent: { id: 'root' }, rawInput: JSON.stringify({ action: 'stop', jobId: 'own' }), signal: abort.signal }); rejected.push(false); } catch { rejected.push(true); }
      console.log(JSON.stringify({ listed, stopped, rejected, killed, recordInput: command.recordInput }));
    `, bridge.name, JSON.stringify(bridge.config)], { windowsHide: true });
    const result = JSON.parse(stdout);
    expect(JSON.parse(result.listed.text)).toEqual([{ id: 'own', ownerSession: 'root', status: 'running' }]);
    expect(JSON.parse(result.stopped.text)).toEqual({ status: 'requested' });
    expect(result.killed).toEqual([{ id: 'own', caller: 'root' }]);
    expect(result.rejected).toEqual([true, true, true, true, true, true, true]);
    expect(result.recordInput).toBe(false);
  } finally { await artifacts.dispose(); }
});
