import { type DeepSeekRemoteClient, isRecord } from '../remote/DeepSeekRemoteClient';
import { type DeepSeekJob, readDeepSeekJobs } from './DeepSeekJobs';

export type { DeepSeekJob } from './DeepSeekJobs';
export interface DeepSeekQueueItem {
  readonly id: string;
  readonly content: readonly unknown[];
  readonly source?: { readonly kind?: string; readonly rpcId?: string };
}
export interface DeepSeekControlState {
  readonly jobs?: readonly DeepSeekJob[];
  readonly queue?: readonly DeepSeekQueueItem[];
}
interface ControlEntry {
  jobs?: DeepSeekJob[];
  queue?: DeepSeekQueueItem[];
  watchers: number;
  revision: number;
  reading?: Promise<void>;
}

export interface DeepSeekAgentRow {
  readonly id: string;
  /** Owning parent of a native subagent. Forks name their source as native parent but are independent roots. */
  readonly parent?: string;
  readonly available: boolean;
  readonly running: boolean;
}

type StoredAgentRow = Omit<DeepSeekAgentRow, 'available'> & { readonly available?: boolean };

type Deliver = (event: Record<string, unknown>) => void;

/**
 * The Host's only subscriber to process-global streams: session roster, control projections and
 * client events. Claimed roots receive the interactions of every agent they own natively.
 */
export class DeepSeekRoster {
  private readonly rows = new Map<string, StoredAgentRow>();
  private readonly projections = new Map<string, Record<string, unknown>>();
  private readonly roots = new Map<string, Deliver>();
  private readonly unrouted = new Map<string, Record<string, unknown>>();
  private readonly changeListeners = new Set<() => void>();
  private readonly resetListeners = new Set<() => void>();
  private subscriptions: Array<() => void> = [];
  private generation = 0;
  private listed = false;
  private baselined = false;
  private readonly controls = new Map<string, ControlEntry>();
  private controlStream?: { off: () => void; ready: Promise<void>; reject: (error: Error) => void };

  constructor(private readonly client: DeepSeekRemoteClient, private readonly onFailure: (error: Error) => void) {}

  get ready(): boolean { return this.listed && this.baselined; }

  /** Opens one baseline generation. Call again after the client reconnects. */
  async start(): Promise<void> {
    this.clear();
    const generation = ++this.generation;
    const pending: unknown[] = [];
    this.subscriptions.push(this.client.onEvent(event => {
      if (generation !== this.generation) return;
      if (this.listed) this.event(event); else pending.push(event);
    }));
    void this.refreshControl().catch(() => {});
    const roster = await this.client.call('session/list', { _request: {} });
    if (generation !== this.generation) return;
    if (!isRecord(roster) || !Array.isArray(roster.items)) throw new Error('Malformed DeepSeek session roster.');
    for (const item of roster.items) this.upsert(item);
    this.listed = true;
    for (const event of pending) this.event(event);
    this.changed();
  }

  /** The transport dropped: all baselines and outstanding native interactions are void. */
  reset(): void {
    ++this.generation;
    this.clear();
    for (const listener of this.resetListeners) listener();
    this.changed();
  }

  row(id: string): DeepSeekAgentRow | undefined {
    const row = this.rows.get(id);
    // Current native summaries omit availability. Only live control evidence or running work
    // makes such a row followable; stored historical subagents remain cold.
    return row ? { ...row, available: row.available ?? (row.running || this.projections.has(id)) } : undefined;
  }
  *allRows(): Iterable<DeepSeekAgentRow> {
    for (const id of this.rows.keys()) yield this.row(id)!;
  }
  projection(id: string): Record<string, unknown> | undefined { return this.projections.get(id); }
  control(id: string): DeepSeekControlState | undefined { return this.controls.get(id); }

  /** Only a followed, activated Agent may admit authenticated exact-owner job reads. */
  watchJobs(id: string): () => void {
    const entry = this.controlEntry(id);
    entry.watchers++;
    void this.refreshJobs(id).catch(error => this.onFailure(error instanceof Error ? error : new Error(String(error))));
    if (entry.queue === undefined) void this.refreshControl().catch(() => {});
    let closed = false;
    return () => {
      if (closed) return;
      closed = true;
      entry.watchers--; entry.revision++;
      if (!entry.watchers) entry.jobs = undefined;
    };
  }

  /** A fresh native baseline is the queue anchor; the bridge supplies exact job ownership. */
  refreshControl(): Promise<void> {
    if (this.controlStream && !this.baselined) return this.controlStream.ready;
    this.controlStream?.off();
    this.baselined = false;
    let resolve!: () => void;
    let reject!: (error: Error) => void;
    const ready = new Promise<void>((yes, no) => { resolve = yes; reject = no; });
    const stream = { off: () => {}, ready, reject };
    this.controlStream = stream;
    const live = (): boolean => this.controlStream === stream;
    const timer = window.setTimeout(() => fail(new Error('DeepSeek control baseline timed out.')), 30_000);
    const fail = (error: Error): void => {
      if (!live()) return;
      window.clearTimeout(timer); this.baselined = false; reject(error); this.onFailure(error);
    };
    void ready.finally(() => window.clearTimeout(timer)).catch(() => {});
    stream.off = this.client.subscribe('session/control', {}, value => {
      if (!live()) return;
      if (!isRecord(value)) throw new Error('Malformed DeepSeek control state.');
      if (value.type === 'baseline' && isRecord(value.value) && isRecord(value.value.projections)) {
        this.projections.clear();
        for (const [id, projection] of Object.entries(value.value.projections)) {
          if (isRecord(projection) && isRecord(projection.values)) this.projections.set(id, projection.values);
        }
        for (const entry of this.controls.values()) entry.queue = undefined;
        if (isRecord(value.value.queues)) for (const [id, queue] of Object.entries(value.value.queues)) {
          this.controlEntry(id).queue = this.decodeQueue(queue);
        }
        const reads = [...this.controls].filter(([, entry]) => entry.watchers > 0).map(([id]) => this.refreshJobs(id));
        void Promise.all(reads).then(() => {
          if (!live()) return;
          this.baselined = true; resolve(); this.changed();
        }, fail);
      } else if (value.type === 'projection' && typeof value.sessionId === 'string' && typeof value.key === 'string') {
        const values = this.projections.get(value.sessionId) ?? {};
        values[value.key] = value.value; this.projections.set(value.sessionId, values);
      } else if (value.type === 'queue' && typeof value.sessionId === 'string') {
        this.controlEntry(value.sessionId).queue = this.decodeQueue(value.items);
      } else if (value.type === 'jobs' && typeof value.sessionId === 'string' && Array.isArray(value.jobs)) {
        const entry = this.controls.get(value.sessionId);
        if (entry?.watchers) void this.refreshJobs(value.sessionId).catch(fail);
      } else throw new Error('Malformed DeepSeek control frame.');
      this.changed();
    }, fail);
    this.changed();
    return ready;
  }

  private controlEntry(id: string): ControlEntry {
    let entry = this.controls.get(id);
    if (!entry) { entry = { watchers: 0, revision: 0 }; this.controls.set(id, entry); }
    return entry;
  }

  private decodeQueue(value: unknown): DeepSeekQueueItem[] {
    if (!Array.isArray(value)) throw new Error('Malformed DeepSeek control queue.');
    return value.map(item => {
      if (!isRecord(item) || typeof item.id !== 'string' || !isRecord(item.message) || !Array.isArray(item.message.content)
        || (item.rpcId !== undefined && typeof item.rpcId !== 'string')) throw new Error('Malformed DeepSeek control queue.');
      return { id: item.id, content: item.message.content,
        ...(typeof item.rpcId === 'string' ? { source: { kind: 'user', rpcId: item.rpcId } } : {}),
      };
    });
  }

  private refreshJobs(id: string): Promise<void> {
    const entry = this.controlEntry(id);
    entry.revision++; entry.jobs = undefined;
    if (entry.reading) return entry.reading;
    const generation = this.generation;
    const live = (): boolean => generation === this.generation && this.controls.get(id) === entry && entry.watchers > 0;
    const read = async (): Promise<void> => {
      while (live()) {
        const revision = entry.revision;
        let jobs: DeepSeekJob[];
        try { jobs = await readDeepSeekJobs(this.client, id); } catch (error) {
          if (!live()) return;
          throw error;
        }
        if (!live()) return;
        if (revision !== entry.revision) continue;
        entry.jobs = jobs; this.changed(); return;
      }
    };
    entry.reading = read().finally(() => { entry.reading = undefined; });
    this.changed();
    return entry.reading;
  }

  /** Nearest claimed ancestor-or-self: the root that owns this agent's work. */
  owner(id: string): string | undefined {
    const seen = new Set<string>();
    for (let current: string | undefined = id; current && !seen.has(current); current = this.rows.get(current)?.parent) {
      if (this.roots.has(current)) return current;
      seen.add(current);
    }
    return undefined;
  }

  /** Exclusive claim of a native session within this Host. */
  claim(rootId: string, deliver: Deliver): () => void {
    if (this.roots.has(rootId)) throw new Error('This DeepSeek conversation is already open in another Claudian view.');
    this.roots.set(rootId, deliver);
    this.changed();
    return () => {
      if (this.roots.get(rootId) !== deliver) return;
      this.roots.delete(rootId);
      this.changed();
    };
  }

  onChange(listener: () => void): () => void { this.changeListeners.add(listener); return () => this.changeListeners.delete(listener); }
  onReset(listener: () => void): () => void { this.resetListeners.add(listener); return () => this.resetListeners.delete(listener); }

  dispose(): void {
    ++this.generation; this.clear(); this.roots.clear();
    this.changeListeners.clear(); this.resetListeners.clear();
  }

  private clear(): void {
    const control = this.controlStream;
    this.controlStream = undefined;
    control?.off(); control?.reject(new Error('DeepSeek control generation ended.'));
    for (const off of this.subscriptions.splice(0)) off();
    this.listed = false; this.baselined = false;
    this.rows.clear(); this.projections.clear(); this.unrouted.clear(); this.controls.clear();
  }

  private upsert(value: unknown): void {
    if (!isRecord(value) || typeof value.sessionId !== 'string' || typeof value.running !== 'boolean'
      || (value.agentAvailable !== undefined && typeof value.agentAvailable !== 'boolean')) throw new Error('Malformed DeepSeek session row.');
    this.rows.set(value.sessionId, {
      id: value.sessionId, running: value.running,
      ...(typeof value.agentAvailable === 'boolean' ? { available: value.agentAvailable } : {}),
      ...(value.origin === 'subagent' && typeof value.parentSessionId === 'string' ? { parent: value.parentSessionId } : {}),
    });
  }

  private event(value: unknown): void {
    if (!isRecord(value)) return;
    if (value.type === 'waterfall' && typeof value.eventId === 'string') {
      if (value.event === 'approval/request' || value.event === 'user-questions/request') this.unrouted.set(value.eventId, value);
    } else if (value.type === 'cancel' && typeof value.eventId === 'string') {
      // Owners ignore unknown identities; a never-routed request simply disappears.
      this.unrouted.delete(value.eventId);
      for (const deliver of [...this.roots.values()]) deliver(value);
    } else if (Array.isArray(value.args)) {
      const [first, second] = value.args as unknown[];
      if (value.event === 'api-session/added') this.upsert(first);
      const row = typeof first === 'string' ? this.rows.get(first) : undefined;
      if (row && value.event === 'api-session/status' && typeof second === 'boolean') this.rows.set(row.id, { ...row, running: second });
      if (row && value.event === 'api-session/removed') this.rows.set(row.id, { ...row, available: false, running: false });
    }
    this.changed();
  }

  private changed(): void {
    // Interactions can precede the roster rows of their agents; route them once ownership is known.
    for (const [eventId, event] of this.unrouted) {
      const owner = typeof event.agentId === 'string' ? this.owner(event.agentId) : undefined;
      if (!owner) continue;
      this.unrouted.delete(eventId);
      this.roots.get(owner)!(event);
    }
    for (const listener of [...this.changeListeners]) listener();
  }
}
