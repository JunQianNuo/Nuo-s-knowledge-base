import { strict as assert } from 'node:assert';
import { mkdtemp, writeFile } from 'node:fs/promises';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
import type { ProviderHost } from '../../src/core/providers/ProviderHost';
import type { ProviderExecutionEvent, ProviderExecutionRequest } from '../../src/core/execution';
import { DeepSeekExecutionBackend } from '../../src/providers/deepseek/execution/DeepSeekExecutionBackend';
import { DeepSeekHost } from '../../src/providers/deepseek/runtime/DeepSeekHost';
import { DeepSeekHostProcess } from '../../src/providers/deepseek/runtime/DeepSeekHostProcess';

Object.assign(globalThis, { window: globalThis });
async function main() {
  const cwd = await mkdtemp(join(tmpdir(), 'claudian-chat-qualification-'));
  await writeFile(join(cwd, 'fixture.txt'), 'TOOL_COMPAT_OK\n');
  const native = new DeepSeekHost(async () => ({ cliPath: 'C:/Users/Nuo/AppData/Roaming/npm/dsh.cmd', cwd, environment: { ...process.env } }), DeepSeekHostProcess.start, 1000);
  const host = { settings: { locale: 'en', providerConfigs: { deepseek: { enabled: true } } } } as unknown as ProviderHost;
  const backend = new DeepSeekExecutionBackend(host, () => native);
  const session = backend.createSession({ lifecycle: 'ephemeral', nativePersistence: 'disabled-if-supported', vaultWorkingDirectory: cwd,
    interactionPort: { requestApproval: async () => ({ decision: 'deny' }), askUserQuestion: async () => ({ answers: {} }), dismissInteraction: () => {} },
  });
  let failure: string | undefined;
  session.onEvent(event => { if (event.type === 'snapshot_changed') return; });
  const run = async (text: string, cancel = false, toolPolicy: ProviderExecutionRequest['toolPolicy'] = { kind: 'provider-default' }) => {
    const signal = AbortSignal.timeout(90000);
    const request: ProviderExecutionRequest = { input: [{ type: 'text', text }],
      configuration: { systemInstructions: { kind: 'explicit', instructions: 'This is an isolated compatibility test. Do not inspect files unless requested. Follow the user request exactly.' }, permissionMode: 'normal' }, toolPolicy, signal };
    const execution = session.execute(request);
    const events: ProviderExecutionEvent[] = [];
    let timer: ReturnType<typeof setTimeout> | undefined;
    try {
      for await (const event of execution.events) {
        events.push(event);
        if (cancel && !timer && event.type === 'turn_started') timer = setTimeout(() => execution.cancel(), 1500);
        if (event.type === 'execution_error') failure = event.message;
      }
    } finally { clearTimeout(timer); }
    assert(!failure, failure);
    assert.equal(events.at(-1)?.type, cancel ? 'cancelled' : 'turn_completed');
    const settledBy = Date.now() + 15000;
    while (session.hasBackgroundWork() && Date.now() < settledBy) await new Promise(resolve => setTimeout(resolve, 20));
    assert(!session.hasBackgroundWork(), 'Execution completed but native background work did not settle');
    const output = JSON.stringify(events);
    if (!cancel) assert(output.includes(text.includes('SECOND_TURN_OK') ? 'SECOND_TURN_OK' : text.includes('TOOL_COMPAT_OK') ? 'TOOL_COMPAT_OK' : 'CHAT_COMPAT_OK'));
    if (text.includes('Read fixture.txt')) assert(events.some(event => event.type === 'tool_completed'));
    console.log(JSON.stringify({ terminal: events.at(-1)?.type, events: events.map(event => event.type), idle: session.getStatus(), background: session.hasBackgroundWork() }));
  };
  try {
    await run('Reply with CHAT_COMPAT_OK only.');
    await run('Reply with SECOND_TURN_OK only.');
    await run('Read fixture.txt using the read tool and reply with its text, TOOL_COMPAT_OK. Do not read any other file.');
    await run('Write a long numbered list of 5000 distinct mathematics topics, one per line. Start now.', true);
  } finally {
    await session.dispose(); await native.dispose();
    console.log(JSON.stringify({ finalFailure: failure ?? null, directory: cwd, modelRequestsLimit: 4 }));
  }
}
main().catch(error => { console.error(error.message); process.exitCode = 1; });
