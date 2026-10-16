/** Reserved, invocation-only command; it never becomes a model-facing tool. */
export const DEEPSEEK_JOB_COMMAND_PREFIX = 'claudian-internal-jobs-';

export const DEEPSEEK_JOB_BRIDGE_SOURCE = String.raw`
export const name = 'claudian-job-control';
export const inject = ['commands', 'jobs'];

export function apply(ctx, config) {
  if (typeof config?.command !== 'string' || !/^claudian-internal-jobs-[a-f0-9-]+$/.test(config.command)) {
    throw new TypeError('Claudian jobs require an invocation command identity.');
  }
  ctx.commands.register({
    name: config.command,
    description: 'Claudian exact-owner background job control',
    input: { hint: '<json>' },
    recordInput: false,
    handler: ({ agent, rawInput, signal }) => {
      signal.throwIfAborted();
      const request = JSON.parse(rawInput);
      if (!request || typeof request !== 'object' || Array.isArray(request)
        || Object.keys(request).some(key => key !== 'action' && key !== 'jobId')) {
        throw new TypeError('Invalid Claudian job request.');
      }
      if (request.action === 'list' && request.jobId === undefined) {
        return { kind: 'success', text: JSON.stringify(ctx.jobs.list(agent).filter(job => job.ownerSession === agent.id)) };
      }
      if (request.action !== 'stop' || typeof request.jobId !== 'string' || !request.jobId || request.jobId.length > 4096) {
        throw new TypeError('Invalid Claudian job action.');
      }
      const job = ctx.jobs.get(request.jobId, agent);
      // Native also exposes ownerless host work. Never admit it to session Stop.
      if (job.ownerSession !== agent.id) throw new Error('Claudian cannot stop a job owned by another session or the Host.');
      const status = ctx.jobs.kill(request.jobId, agent, 'Stopped by Claudian');
      return { kind: 'success', text: JSON.stringify({ status }) };
    },
  });
}
`;
