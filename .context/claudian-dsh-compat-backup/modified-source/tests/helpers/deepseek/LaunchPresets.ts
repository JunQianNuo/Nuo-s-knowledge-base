import { readdir,readFile } from 'node:fs/promises';
import { join } from 'node:path';

/** Read the invocation-only compositions through native's public preset roster. */
export async function readLaunchPresets(patchPath: string): Promise<Record<string, any[]>> {
  const patch = JSON.parse(await readFile(patchPath, 'utf8'));
  const roster = patch.find((entry: { id?: string }) => entry.id === 'agent-presets');
  if (!roster) throw new Error('The launch overlay has no file-based agent preset roster.');
  const root = roster.config.roots[0].path;
  return Object.fromEntries(await Promise.all((await readdir(root)).map(async preset => [
    preset, JSON.parse(await readFile(join(root, preset, 'agent.cordis.yml'), 'utf8')),
  ])));
}
