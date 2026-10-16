export const name = 'claudian-native-job-fixture';
export const inject = ['commands', 'jobs'];
export function apply(ctx) {
  ctx.commands.register({
    name: 'claudian-fixture-job-start', description: 'Create one controlled native qualification job', recordInput: false,
    handler: ({ agent, signal }) => {
      signal.throwIfAborted();
      const jobId = ctx.jobs.start({ owner: agent, kind: 'compat-fixture', label: 'Claudian controlled qualification job',
        run: () => {
          let settle;
          const done = new Promise(resolve => { settle = resolve; });
          return { done, cancel: () => setTimeout(() => settle({ status: 'killed', output: 'qualification job stopped' }), 30) };
        },
      });
      return { kind: 'success', text: JSON.stringify({ jobId }) };
    },
  });
}
