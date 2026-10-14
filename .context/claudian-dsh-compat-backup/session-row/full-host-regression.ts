import { strict as assert } from 'node:assert';
import { DeepSeekHost } from '../src/providers/deepseek/runtime/DeepSeekHost';
import { DeepSeekHostProcess } from '../src/providers/deepseek/runtime/DeepSeekHostProcess';
Object.assign(globalThis,{window:globalThis});
async function main(){
 const host = new DeepSeekHost(async()=>({cliPath:'C:/Users/Nuo/AppData/Roaming/npm/dsh.cmd',cwd:'D:/知识库',environment:{...process.env}}),DeepSeekHostProcess.start,1000);
 try {
  const lease = await host.attach(AbortSignal.timeout(90000));
  try {
   const deadline=Date.now()+3000;while(!lease.roster.ready){if(Date.now()>deadline)throw Error('Full Host control baseline did not become ready');await new Promise(resolve=>setTimeout(resolve,10));}
   const catalog=await host.read(reader=>reader.call('session/modelCatalog')) as {groups:{id:string;models:{id:string}[]}[]};
   assert(catalog.groups.some(group=>group.models.length));
   console.log(JSON.stringify({fullHostReady:lease.roster.ready,sessionRows:Array.from(lease.roster.allRows()).length,models:catalog.groups.map(group=>({provider:group.id,models:group.models.map(model=>model.id)}))}));
   for(const agentPreset of ['claudian','claudian-code','claudian-passive','claudian-read-only']){const sessionId=lease.ephemeralSessionId();const created=await lease.client.call('session/create',{request:{sessionId,cwd:'D:/知识库',agentPreset}}) as {sessionId:string};assert.equal(created.sessionId,sessionId);}
   console.log(JSON.stringify({blankPresetSessionsCreated:4,actualModelTurnsTested:false}));
  } finally {lease.release();}
 } finally {await host.dispose();}
}
main().catch(error=>{console.error(error.message);process.exitCode=1});
