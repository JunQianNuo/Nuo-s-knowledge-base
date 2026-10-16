export function apply(ctx) {
  ctx.inject(['typertGateway'], c => {
    const endpoints = [
      'session/list', 'session/control', 'session/create', 'session/follow',
      'session/page', 'session/projections', 'session/prompt', 'session/cancel',
      'session/updateQueue', 'job/list', 'job/kill', 'commands/list',
      'commands/execute', 'permissionPresets/catalog', 'skills/list',
      'subagents/interruptByParent',
    ];
    const show = () => console.log('CHAT_CONTRACT ' + JSON.stringify({
      claims: endpoints.map(endpoint => ({ endpoint, registered: c.typertGateway.claimsEndpoint(endpoint) })),
      services: ['sessionController', 'jobs', 'commands', 'permissionPresets'].map(name => ({
        name, present: ctx.get(name) !== undefined,
      })),
      jobRemoteExports: [...c.typertGateway.collectSrcClaims()].filter(endpoint => /^jobs?\//.test(endpoint)),
      permissionPresetNames: ctx.get('permissionPresets')?.names ?? [],
    }));
    setTimeout(show, 2000).unref();
  });
}
