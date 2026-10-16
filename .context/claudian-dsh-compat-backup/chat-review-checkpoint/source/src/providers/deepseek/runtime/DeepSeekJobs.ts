import { type DeepSeekReader, isRecord } from '../remote/DeepSeekRemoteClient';
import { DEEPSEEK_JOB_COMMAND_PREFIX } from './DeepSeekJobBridge';

export interface DeepSeekJob { readonly id: string; readonly owner: string; readonly status: string }

export async function callDeepSeekJobs(client: DeepSeekReader, sessionId: string, request: { action: 'list' } | { action: 'stop'; jobId: string }, signal?: AbortSignal): Promise<unknown> {
  const options = { signal: signal ? AbortSignal.any([signal, AbortSignal.timeout(10_000)]) : AbortSignal.timeout(10_000) };
  const commands = await client.call('commands/list', { agentId: sessionId }, options);
  const candidates: Record<string, unknown>[] = Array.isArray(commands) ? commands.filter((command: unknown): command is Record<string, unknown> => isRecord(command)
    && typeof command.name === 'string' && command.name.startsWith(DEEPSEEK_JOB_COMMAND_PREFIX)) : [];
  const name = candidates[0]?.name;
  if (candidates.length !== 1 || typeof name !== 'string') throw new Error('DeepSeek exact-owner job control is unavailable. Restart the conversation with the current Claudian preset.');
  const result = await client.call('commands/execute', { agentId: sessionId, line: `/${name} ${JSON.stringify(request)}`, submittedAttachments: [] }, options);
  if (!isRecord(result) || !isRecord(result.result) || result.result.kind !== 'success' || typeof result.result.text !== 'string') {
    throw new Error('DeepSeek exact-owner job control failed.');
  }
  try { return JSON.parse(result.result.text); } catch { throw new Error('Malformed DeepSeek exact-owner job result.'); }
}

export async function readDeepSeekJobs(client: DeepSeekReader, sessionId: string): Promise<DeepSeekJob[]> {
  const result = await callDeepSeekJobs(client, sessionId, { action: 'list' });
  if (!Array.isArray(result)) throw new Error('Malformed DeepSeek exact-owner jobs.');
  return result.map(job => {
    if (!isRecord(job) || typeof job.id !== 'string' || typeof job.status !== 'string' || job.ownerSession !== sessionId) {
      throw new Error('Malformed or foreign DeepSeek job.');
    }
    return { id: job.id, owner: sessionId, status: job.status };
  });
}

export async function stopDeepSeekJob(client: DeepSeekReader, job: DeepSeekJob, signal?: AbortSignal): Promise<void> {
  const result = await callDeepSeekJobs(client, job.owner, { action: 'stop', jobId: job.id }, signal);
  if (!isRecord(result) || (result.status !== 'requested' && result.status !== 'already-finished')) {
    throw new Error('DeepSeek did not acknowledge the owned job stop.');
  }
}
