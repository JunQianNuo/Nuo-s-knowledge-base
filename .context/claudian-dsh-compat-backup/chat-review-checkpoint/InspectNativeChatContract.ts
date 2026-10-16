import { spawn } from 'node:child_process';
import { readFile, writeFile } from 'node:fs/promises';
import { prepareDeepSeekLaunchArtifacts } from '../../src/providers/deepseek/runtime/DeepSeekLaunchArtifacts';

Object.assign(globalThis, { window: globalThis });
async function main() {
  const artifacts = await prepareDeepSeekLaunchArtifacts();
  let child: ReturnType<typeof spawn> | undefined;
  let exited: Promise<unknown> | undefined;
  try {
    const patch = JSON.parse(await readFile(artifacts.patchPath, 'utf8'));
    patch.push({ insert: [{ id: 'chat-contract-diagnostic', name: 'C:/Users/Nuo/AppData/Local/Temp/claudian-dsh-compat-work/.context/deepseek-chat-execution/InspectNativeChatContract.mjs' }] });
    await writeFile(artifacts.patchPath, JSON.stringify(patch));
    child = spawn('D:/Node.js/node.exe', [
      'C:/Users/Nuo/AppData/Roaming/npm/node_modules/@deepseek-ai/dsh/lib/bin.js',
      '--profile', 'web', '--patch', artifacts.patchPath, '--no-open', '--port', '0',
    ], { cwd: 'D:/知识库', windowsHide: true, stdio: ['pipe', 'pipe', 'pipe'] });
    exited = new Promise(resolve => child!.once('exit', resolve));
    const report = await new Promise<string>((resolve, reject) => {
      let buffer = '';
      const timer = setTimeout(() => reject(Error('Native contract probe timed out')), 60000);
      const data = (bytes: Buffer) => {
        buffer += bytes.toString('utf8');
        const match = buffer.match(/CHAT_CONTRACT (\{[^\r\n]+\})/);
        if (match) { clearTimeout(timer); resolve(match[1]); }
      };
      child!.stdout!.on('data', data); child!.stderr!.on('data', data);
      child!.once('error', error => { clearTimeout(timer); reject(error); });
      child!.once('exit', () => { clearTimeout(timer); reject(Error('Native exited before contract report')); });
    });
    const json = JSON.parse(report);
    await writeFile('C:/Users/Nuo/AppData/Local/Temp/claudian-dsh-compat-work/.context/deepseek-chat-execution/native-chat-contract.json', JSON.stringify(json, null, 2));
    console.log(JSON.stringify(json));
  } finally {
    if (child && exited) {
      child.stdin?.end();
      let timer: ReturnType<typeof setTimeout> | undefined;
      await Promise.race([exited, new Promise<void>(resolve => { timer = setTimeout(() => { child!.kill(); resolve(); }, 6000); })]);
      clearTimeout(timer);
    }
    await artifacts.dispose();
  }
}
main().catch(error => { console.error(error.message); process.exitCode = 1; });
