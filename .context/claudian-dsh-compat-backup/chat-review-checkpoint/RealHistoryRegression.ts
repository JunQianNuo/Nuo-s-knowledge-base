import { strict as assert } from 'node:assert';
import { mkdtemp } from 'node:fs/promises';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
import type { ProviderHost } from '../../src/core/providers/ProviderHost';
import type { ProviderExecutionEvent, ProviderExecutionSession, ProviderSessionConfig } from '../../src/core/execution';
import { DeepSeekExecutionBackend } from '../../src/providers/deepseek/execution/DeepSeekExecutionBackend';
import { DeepSeekConversationHistoryService } from '../../src/providers/deepseek/history/DeepSeekConversationHistoryService';
import { DeepSeekHost } from '../../src/providers/deepseek/runtime/DeepSeekHost';
import { DeepSeekHostProcess } from '../../src/providers/deepseek/runtime/DeepSeekHostProcess';
Object.assign(globalThis, { window: globalThis });
async function main() {
  const cwd = await mkdtemp(join(tmpdir(), 'claudian-history-qualification-'));
  const createHost = () => new DeepSeekHost(async () => ({ cliPath: 'C:/Users/Nuo/AppData/Roaming/npm/dsh.cmd', cwd, environment: { ...process.env } }), DeepSeekHostProcess.start, 1000);
  const provider = { settings: { locale: 'en', providerConfigs: { deepseek: { enabled: true } } } } as unknown as ProviderHost;
  const config: ProviderSessionConfig = { lifecycle: 'persistent', nativePersistence: 'enabled', vaultWorkingDirectory: cwd,
    interactionPort: { requestApproval: async () => ({ decision: 'deny' }), askUserQuestion: async () => ({ answers: {} }), dismissInteraction: () => {} },
  };
  const send = async (session: ProviderExecutionSession, marker: string) => {
    const run = session.execute({ input: [{ type: 'text', text: `Reply with ${marker} only.` }],
      configuration: { permissionMode: 'normal', systemInstructions: { kind: 'explicit', instructions: 'Isolated synthetic compatibility test. Do not access any files or tools.' } },
      toolPolicy: { kind: 'provider-default' }, signal: AbortSignal.timeout(90000) });
    const events: ProviderExecutionEvent[] = [];
    for await (const event of run.events) events.push(event);
    const failed = events.find(event => event.type === 'execution_error');
    assert(!failed, failed && 'message' in failed ? failed.message : 'Execution failed');
    assert.equal(events.at(-1)?.type, 'turn_completed'); assert(JSON.stringify(events).includes(marker));
  };
  let host = createHost();
  let session = new DeepSeekExecutionBackend(provider, () => host).createSession(config);
  try {
    await send(session, 'HISTORY_COMPAT_OK');
    const saved = session.getSnapshot();
    assert(saved.providerSessionId && saved.providerState);
    await session.dispose(); await host.dispose();
    host = createHost();
    const history = new DeepSeekConversationHistoryService(async () => host);
    const restored = await history.hydrateConversationHistory({ sessionId: saved.providerSessionId, providerState: saved.providerState, messages: [] }, cwd);
    assert(restored.messages?.some(message => message.role === 'assistant' && message.content.includes('HISTORY_COMPAT_OK')));
    session = new DeepSeekExecutionBackend(provider, () => host).createSession({ ...config, resumeSeed: { providerSessionId: saved.providerSessionId, providerState: saved.providerState } });
    await send(session, 'RESUME_COMPAT_OK');
    console.log(JSON.stringify({ coldHistory: 'PASS', resumedExecution: 'PASS', syntheticSessionCreated: saved.providerSessionId, modelRequestsSent: 2 }));
  } finally { await session.dispose(); await host.dispose(); }
}
main().catch(error => { console.error(error.message); process.exitCode = 1; });
