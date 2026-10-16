import { normalizeImageMediaType } from '@/core/execution/imageAttachment';
import type { ImageAttachment } from '@/core/types';

import { deepseekToolResult } from '../normalization/DeepSeekOutput';
import { type DeepSeekReader,isRecord } from '../remote/DeepSeekRemoteClient';

export async function readDeepSeekImages(client: DeepSeekReader, sessionId: string, content: unknown): Promise<ImageAttachment[]> {
  if (!Array.isArray(content)) return [];
  const images: ImageAttachment[] = [];
  for (const block of content) {
    if (!isRecord(block) || block.type !== 'image') continue;
    if (!isRecord(block.attachment) || typeof block.attachment.attachmentId !== 'string' || !block.attachment.attachmentId) {
      throw new Error('Malformed DeepSeek image reference.');
    }
    const response = await client.call('session/attachment', { request: { sessionId, attachmentId: block.attachment.attachmentId } });
    if (!isRecord(response) || !isRecord(response.attachment) || response.attachment.attachmentId !== block.attachment.attachmentId || typeof response.data !== 'string') throw new Error('Malformed DeepSeek image attachment.');
    const attachment = response.attachment;
    const mediaType = normalizeImageMediaType(attachment.mediaType);
    if (!mediaType) throw new Error('Unsupported DeepSeek image media type.');
    images.push({ id: block.attachment.attachmentId, name: typeof attachment.name === 'string' ? attachment.name : 'DeepSeek image',
      mediaType, data: response.data,
      size: Buffer.byteLength(response.data, 'base64'), source: 'file',
    });
  }
  return images;
}

export async function materializeDeepSeekToolImages<T extends { type?: unknown; data?: unknown }>(client: DeepSeekReader, sessionId: string, event: T): Promise<T> {
  if (event.type !== 'tool/result' || !isRecord(event.data) || !isRecord(event.data.message)) return event;
  const result = deepseekToolResult(event.data.message);
  if (!result) return event;
  const images = await readDeepSeekImages(client, sessionId, result.content);
  if (!images.length) return event;
  const content = [...(Array.isArray(result.content) ? result.content as unknown[] : []), ...images.map(image => ({ type: 'image', mediaType: image.mediaType, data: image.data, name: image.name }))];
  const message = typeof event.data.message.toolCallId === 'string'
    ? { ...event.data.message, content }
    : { ...event.data.message, content: (event.data.message.content as unknown[]).map(block => block === result ? { ...result, content } : block) };
  return { ...event, data: { ...event.data, message } };
}
