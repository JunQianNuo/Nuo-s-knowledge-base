"""Explicit legacy-to-v2 placement and metadata proposals; never writes the Vault."""
from __future__ import annotations

from collections import Counter, defaultdict
from datetime import datetime, timedelta, timezone
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import posixpath
import re
import subprocess
from urllib.parse import quote, unquote, urlsplit

import link_validator
from . import model

TZ = timezone(timedelta(hours=8))
CORE = ('概念', '知识点', '方法')
IMAGE_EXTS = {'.png', '.jpg', '.jpeg', '.svg', '.gif', '.webp', '.bmp'}
HOMEWORK = {'习题','例题','证明题','思考题','作业','考题','模拟试卷','测验解答','作业解答','课堂测试解答','homework'}
REVIEWS = {'知识梳理','答疑','复习','速查','复习纲要','考试纲要','知识点','概念辨析','review'}
RESOURCES = {'MOC','知识图谱','规范','审查报告','知识库参考','资料核对','资料','课件笔记'}
MATH_TOPICS = {'收敛性与积分理论','数值计算','最优化','概率与随机结构','集合与空间'}


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def _files(root, scope, extensions=None):
    start = root / scope
    if not start.exists():
        return
    if start.is_file():
        yield start
        return
    for folder, dirs, files in os.walk(start, followlinks=False):
        parent = Path(folder)
        dirs[:] = sorted(n for n in dirs if not n.startswith('.') and n != '__pycache__'
                         and not link_validator.protected_reason(root, parent/n))
        for name in sorted(files):
            p = parent/name
            if extensions is not None and p.suffix.lower() not in extensions:
                continue
            if not name.startswith('.') and not link_validator.protected_reason(root,p):
                yield p


def _list(value):
    return value if isinstance(value,list) else [] if value in (None,'') else [value]


def _course(relative):
    parts = PurePosixPath(relative).parts[1:]
    cut = 2 if parts and parts[0] == '归档' and len(parts)>1 else 1
    return '/'.join(parts[:cut]), parts[cut-1] if parts else '', parts[cut:]


def creation_history(root):
    """First recorded Git time, carrying identity through tracked renames."""
    root=Path(root)
    if not (root/'.git').exists():
        return {}
    result=subprocess.run(['git','-c','core.quotepath=false','log','--reverse','--format=@@%aI','--name-status','--find-renames'],
                          cwd=root,capture_output=True,text=True,encoding='utf-8',check=True,timeout=30)
    active={};stamp=None
    for line in result.stdout.splitlines():
        if line.startswith('@@'):
            stamp=line[2:];continue
        values=line.split('\t')
        if stamp is None or len(values)<2:
            continue
        status=values[0]
        if status.startswith('R') and len(values)==3:
            previous=active.pop(values[1],{'time':stamp,'origin':values[1]})
            active[values[2]]=previous
        elif status=='A':
            active[values[1]]={'time':stamp,'origin':values[1]}
        elif status=='D':
            active.pop(values[1],None)
    return {name:value for name,value in active.items() if name.lower().endswith('.md')}


def _stamp(path, data, report):
    for key in ('time','created','created_at'):
        value = data.get(key)
        if isinstance(value,str):
            try:
                stamp = datetime.fromisoformat(value.replace('Z','+00:00'))
                if stamp.tzinfo is None:
                    stamp = stamp.replace(tzinfo=TZ)
                report['time_basis'][str(path)] = key
                return stamp.isoformat(timespec='seconds')
            except ValueError:
                pass
    history=report.get('_history',{}).get(str(path))
    if history:
        report['time_basis'][str(path)]='git_first_recorded:'+history['origin']
        return datetime.fromisoformat(history['time']).isoformat(timespec='seconds')
    stamp = datetime.fromtimestamp(path.stat().st_birthtime, TZ)
    report['time_basis'][str(path)] = 'filesystem_birthtime; may postdate initial authorship'
    return stamp.isoformat(timespec='seconds')


def rewrite_links(text, old_name, new_name, mapping, shortnames):
    """Change only recognized links, preserving code, mathematics and all other text."""
    if old_name.lower().endswith('.canvas'):
        document=json.loads(text)
        targets={node.get('file') for node in document.get('nodes',[]) if node.get('type')=='file'}
        def canvas_file(match):
            original=json.loads(match.group(1))
            if original in targets and original in mapping:
                return match.group(0)[:match.start(1)-match.start()] + json.dumps(mapping[original],ensure_ascii=False)
            return match.group(0)
        return re.sub(r'"file"\s*:\s*("(?:[^"\\]|\\.)*")',canvas_file,text)
    active = link_validator._active_text(text)
    edits = []
    def wiki(match):
        if link_validator._escaped(text,match.start()):
            return
        value = match.group(1)
        target, *alias = value.split('|',1)
        alias_separator = '\\|' if alias and target.endswith('\\') else '|'
        if alias_separator == '\\|':
            target = target[:-1]
        target, sep, anchor = target.partition('#')
        key = target if target.lower().endswith('.md') else target + '.md'
        resolved = key if key in mapping else shortnames.get(key)
        if resolved is None:
            # Assets have explicit suffixes; do not append .md to those.
            resolved = target if target in mapping else shortnames.get(target)
        if resolved is None and PurePosixPath(target).suffix.lower() not in ('','.md'):
            sibling=posixpath.normpath(posixpath.join(posixpath.dirname(old_name),target))
            if sibling in mapping:
                resolved=sibling
        if resolved not in mapping:
            return
        new = mapping[resolved]
        if new.lower().endswith('.md') and not target.lower().endswith('.md'):
            new = new[:-3]
        suffix = (sep + anchor) if sep else ''
        if alias:
            suffix += alias_separator + alias[0]
        edits.append((match.start(1),match.end(1),new+suffix))
    for match in re.finditer(r'\[\[([^\]\r\n]+)\]\]', active):
        wiki(match)
    # URI-bearing Markdown and HTML use the source directory, unlike Wiki-links.
    spans=[]
    starts=[match.end() for match in re.finditer(r'\]\(',active) if not link_validator._escaped(text,match.start())]
    starts += [match.end() for match in re.finditer(r'(?m)^[ \t]{0,3}\[[^\]\r\n]+\]:[ \t]*',active)]
    for start in starts:
        while start<len(active) and active[start] in ' \t':
            start+=1
        end=start
        if start<len(active) and active[start]=='<':
            end=active.find('>',start+1)
            if end<0:continue
            end+=1
        else:
            depth=0
            while end<len(active):
                ch=active[end]
                if ch=='\\' and end+1<len(active):
                    end+=2;continue
                if ch=='(':
                    depth+=1
                elif ch==')':
                    if not depth:break
                    depth-=1
                elif ch.isspace():
                    break
                end+=1
        if end>start:
            spans.append((start,end))
    for match in re.finditer(r'\b(?:src|href)\s*=\s*["\'](?P<uri>[^"\']+)["\']',active):
        spans.append((match.start('uri'),match.end('uri')))
    for start,end in sorted(set(spans)):
            original = text[start:end]
            angle = original.startswith('<') and original.endswith('>')
            uri = original[1:-1] if angle else original
            split = urlsplit(uri)
            if split.scheme or split.netloc or not split.path or split.path.startswith('#'):
                continue
            decoded = re.sub(r'\\([() <>])',r'\1',unquote(split.path)).replace('\\','/')
            old_target = posixpath.normpath(decoded.lstrip('/') if decoded.startswith('/') else posixpath.join(posixpath.dirname(old_name),decoded))
            new_target = mapping.get(old_target)
            # Even an unmoved attachment needs a new relative URI when its note moves.
            if new_target is None and old_name != new_name:
                new_target = old_target
            if new_target is None:
                continue
            relative = posixpath.relpath(new_target,posixpath.dirname(new_name) or '.')
            if relative == decoded:
                continue  # Preserve unchanged relative attachment URIs verbatim.
            changed = quote(relative,safe='/._-~')
            if split.query:
                changed += '?' + split.query
            if split.fragment:
                changed += '#' + split.fragment
            if angle:
                changed = '<' + changed + '>'
            if changed != original:
                edits.append((start,end,changed))
    result = text
    for start,end,value in sorted(edits,reverse=True):
        result = result[:start] + value + result[end:]
    return result


def _base_metadata(path, data, kind, report):
    data = dict(data)
    title = data.pop('title',None)
    if title and title != path.stem and isinstance(title,str):
        aliases = _list(data.get('aliases'))
        if title not in aliases:
            aliases.append(title)
        data['aliases'] = aliases
    data['schema_version'] = 2
    data['type'] = kind
    data['time'] = _stamp(path,data,report)
    for field in ('aliases','tags'):
        data[field] = _list(data.get(field))
    if data.get('status') not in (None,'not done','done'):
        data['legacy_status'] = data.pop('status')
    if kind in model.ATOMIC_TYPES:
        if 'subject' in data:
            data['legacy_subject']=data.pop('subject')
    if kind in model.SOURCE_TYPES:
        if 'topics' in data:
            data['legacy_topics'] = data.pop('topics')
        data['source'] = _list(data.get('source'))
        data['status'] = 'not done'
    return data


def _inbox(data, reason):
    data = dict(data)
    if 'type' in data:
        data['legacy_type'] = data.pop('type')
    if 'schema_version' in data:
        data['legacy_schema_version'] = data.pop('schema_version')
    data['migration_reason'] = reason
    return data


def build(root: Path, decisions=None):
    root = Path(root).resolve()
    decisions = decisions or {}
    records, mapping = {}, {}
    report = {'time_basis':{},'inbox':[],'sources':[],'outside_link_updates':[],'semantic_evidence':[], 'unresolved_relations':[]}
    try:
        report['_history']={str(root/name):value for name,value in creation_history(root).items()}
    except (OSError,subprocess.SubprocessError) as error:
        report['history_warning']=str(error)
    for scope in (*CORE,'课程','总览/标签库'):
        for path in _files(root,scope):
            name = path.relative_to(root).as_posix()
            raw = path.read_bytes() if path.suffix.lower()=='.md' else None
            data,body = model.read_note(raw) if raw is not None else ({},None)
            records[name] = {'path':path,'data':data,'body':body,'raw':raw,'kind':None}
    # Only explicit current theme MOCs belong to this migration, not other projects' MOCs.
    for path in sorted((root/'总览').glob('*.md')) if (root/'总览').exists() else []:
        if link_validator.protected_reason(root,path):
            continue
        raw = path.read_bytes()
        data,body = model.read_note(raw)
        if data.get('role')=='moc' or path.stem in ('课程-MOC','知识库主页'):
            records[path.relative_to(root).as_posix()]={'path':path,'data':data,'body':body,'raw':raw,'kind':None}
    tag_base=root/'总览/标签库.base'
    if tag_base.is_file() and not link_validator.protected_reason(root,tag_base):
        records['总览/标签库.base']={'path':tag_base,'data':{},'body':None,'raw':tag_base.read_bytes(),'kind':None}
    for name,decision in decisions.items():
        if (name not in records or PurePosixPath(name).parts[0] not in CORE or not isinstance(decision,dict)
                or decision.get('disposition') not in ('knowledge','inbox')
                or not re.fullmatch(r'[0-9a-f]{64}',decision.get('note_sha256',''))
                or decision['note_sha256']!=sha(records[name]['raw'])):
            raise ValueError('Invalid or stale hash-bound semantic decision: '+name)
        if decision['disposition']=='knowledge':
            if decision.get('type') not in model.ATOMIC_TYPES or not isinstance(decision.get('sources'),list) or not decision['sources']:
                raise ValueError('Knowledge decision needs typed, verified sources: '+name)
            evidence=decision.get('evidence',[])
            for source in decision['sources']:
                if (not isinstance(source,str) or not source.startswith('课程/') or '..' in source.split('/')
                        or link_validator.protected_reason(root,root/source)):
                    raise ValueError('Invalid semantic source path')
                matching=[e for e in evidence if e.get('path')==source and re.fullmatch(r'[0-9a-f]{64}',e.get('sha256',''))]
                if not matching or any(sha((root/source).read_bytes())!=e['sha256'] for e in matching):
                    raise ValueError('Source evidence missing or stale: '+source)
    for name,record in records.items():
        path,data = record['path'],record['data']
        parts=PurePosixPath(name).parts
        if name=='总览/标签库.base':
            target='99_System/knowledge/tags/标签库.base'
        elif name.startswith('总览/标签库/'):
            target='99_System/knowledge/tags/'+name[len('总览/标签库/'):]
        elif parts[0] in CORE:
            decision=decisions.get(name)
            if decision and decision.get('note_sha256') and decision['note_sha256']!=sha(record['raw']):
                raise ValueError('Semantic decision stale: '+name)
            if data.get('type')=='MOC':
                target='99_System/knowledge/legacy_navigation/'+parts[0]+'-'+path.name
            else:
                kind=decision.get('type') if decision else data.get('type')
                pending = (decision and decision.get('disposition')=='inbox') or kind not in model.ATOMIC_TYPES
                if pending:
                    reason=decision.get('reason','Requires semantic review') if decision else 'Requires semantic review'
                    record['pending']=reason
                    target='00_Inbox/待核实核心/'+parts[0]+'/'+path.name
                else:
                    record['kind']=kind
                    target='01_Knowledge/'+path.name
        elif parts[0]=='课程':
            branch,subject,tail=_course(name)
            raw_tree=any(part.casefold() in {'raw','ppt','ppt课件','课件','pdf','md','板书','未处理项'} for part in tail[:-1])
            kind=data.get('type')
            if path.suffix.lower() in IMAGE_EXTS:
                target='03_Sources/Courses/'+branch+'/'+('/'.join(tail))
            else:
                note_kind=None if raw_tree or kind in RESOURCES else ('lecture' if kind in ('课堂笔记','lecture') else 'homework' if kind in HOMEWORK else 'review' if kind in REVIEWS else None)
                record['kind']=note_kind
                record['subject']=subject
                record['branch']=branch
                changed_tail=list(tail)
                if note_kind=='homework' and changed_tail and changed_tail[0] in ('习题库','习题','作业'):
                    changed_tail[0]='作业'
                target=('03_Sources/Reviews/' if note_kind=='review' else '03_Sources/Courses/')+branch+'/'+('/'.join(changed_tail))
        else:
            if data.get('role')=='moc' and path.stem not in ('核心知识工作台','知识网络-MOC'):
                stem=path.stem.removesuffix('-MOC')
                target='02_Maps/MOC-'+stem+'.md'
                record['kind']='moc'
            else:
                target='99_System/knowledge/legacy_navigation/'+path.name
        mapping[name]=target
    # Assign Sources metadata before checking atomic provenance against projected identities.
    for name,record in records.items():
        kind=record['kind']
        if kind in model.SOURCE_TYPES:
            data=_base_metadata(record['path'],record['data'],kind,report)
            data['subject']=list(dict.fromkeys(_list(data.get('subject')) or [record['subject']]))
            if kind=='lecture':
                old_status=record['data'].get('status')
                if old_status is not None or 'record_file_id' in data:
                    data['polish_status']='done' if old_status in ('已完成','已补全（无逐字稿）') else 'not done'
                value=data.get('date')
                if isinstance(value,str) and re.match(r'^\d{4}-\d{2}-\d{2}',value):
                    data['lecture_date']=value[:10]
            if not data['source']:
                record['pending']='Missing traceable source in legacy source note'
                mapping[name]='00_Inbox/待核实来源/'+name[len('课程/'):]
                data=_inbox(data,record['pending'])
                record['kind']=None
            record['new_data']=data
    source_names={name for name,record in records.items() if record['kind'] in model.SOURCE_TYPES}
    # Parent notes are infrastructure choices, while existing specific themes retain their manual bodies.
    new_notes={}
    for label in ('数学','物理','计算机科学','深度学习','数理统计'):
        path='02_Maps/MOC-'+label+'.md'
        if path in mapping.values() or (root/path).exists():
            continue
        parents=['[[02_Maps/MOC-计算机科学]]'] if label=='深度学习' else ['[[02_Maps/MOC-数学]]'] if label=='数理统计' else []
        new_notes[path]=model.render_note({'schema_version':2,'type':'moc','time':datetime.now(TZ).isoformat(timespec='seconds'),'topics':parents,'aliases':[],'tags':[]},('# '+label+'\n\n学科与主题导航。\n').encode())
    for name,record in records.items():
        kind=record['kind']
        if kind=='moc':
            data=_base_metadata(record['path'],record['data'],kind,report)
            data.pop('role',None)
            label=record['path'].stem.removesuffix('-MOC')
            data['topics']=['[[02_Maps/MOC-数学]]'] if label in MATH_TOPICS else ['[[02_Maps/MOC-物理]]'] if label=='热学与量子' else []
            # MOC source was optional in v1; don't leave an invalid empty source property.
            if not data.get('source'):
                data.pop('source',None)
            record['new_data']=data
        elif kind in model.ATOMIC_TYPES:
            decision=decisions.get(name,{})
            data=_base_metadata(record['path'],record['data'],kind,report)
            sources=_list(data.get('source'))
            for evidence in decision.get('evidence',[]):
                p=root/evidence['path']
                if evidence.get('sha256') and sha(p.read_bytes())!=evidence['sha256']:
                    raise ValueError('Source evidence stale: '+evidence['path'])
            for item in decision.get('sources',[]):
                value='[['+item.removesuffix('.md')+']]'
                if value not in sources:
                    sources.append(value)
            good=[]
            for value in sources:
                target=model.link_target(value)
                matches=[key for key in source_names if target and (key==target or ('/' not in target and PurePosixPath(key).name==target))]
                if len(matches)==1:
                    good.append(value)
            topics=[value for value in _list(data.get('topics')) if model.link_target(value) in mapping and mapping[model.link_target(value)].startswith('02_Maps/')]
            if not topics and good:
                names=' '.join(good)
                label='概率与随机结构' if '概率论' in names or '统计' in names else '数值计算' if '数值分析' in names else '最优化' if '最优化' in names else '热学与量子' if '物理' in names else '收敛性与积分理论'
                target=next((key for key in mapping.values() if key=='02_Maps/MOC-'+label+'.md'),'02_Maps/MOC-数学.md')
                topics=['[['+target.removesuffix('.md')+']]']
            rejected=[value for value in sources if value not in good]
            if rejected:
                data['legacy_source']=list(dict.fromkeys(_list(data.get('legacy_source'))+rejected))
            old_topics=[value for value in _list(data.get('topics')) if value not in topics]
            if old_topics:
                data['legacy_topics']=list(dict.fromkeys(_list(data.get('legacy_topics'))+old_topics))
            data['source']=list(dict.fromkeys(good))
            data['topics']=list(dict.fromkeys(topics))
            if not good:
                record['pending']='Missing valid Sources-note provenance; raw assets alone do not qualify'
                mapping[name]='00_Inbox/待核实核心/'+name
                data=_inbox(data,record['pending'])
                record['kind']=None
            record['new_data']=data
            if decision:
                report['semantic_evidence'].append(name)
    # Stabilize unique target names before any link replacement.
    occupied={}
    for old,target in sorted(mapping.items()):
        key=target.casefold()
        if key in occupied:
            p=PurePosixPath(target)
            target=str(p.with_name(p.stem+'（'+PurePosixPath(old).parts[0]+'）'+p.suffix))
            if target.casefold() in occupied:
                raise ValueError('Unresolved target collision: '+old)
            mapping[old]=target
        occupied[mapping[old].casefold()]=old
    short=defaultdict(list)
    # Wiki-link ambiguity belongs to the whole visible namespace, not just moved files.
    for path in _files(root,'.',extensions={'.md'}):
        short[path.name].append(path.relative_to(root).as_posix())
    short={key:values[0] for key,values in short.items() if len(values)==1}
    def change(text,old,new):
        return rewrite_links(text,old,new,mapping,short)
    operations=[]
    for name,record in records.items():
        target=mapping[name]
        data=record.get('new_data')
        if record.get('pending'):
            if data is None:
                data=_inbox(record['data'],record['pending'])
            report['inbox'].append({'source':name,'target':target,'reason':record['pending']})
        if data is not None:
            # Existing unresolved dependencies are preserved as legacy fields, not invented links.
            for field in ('uses','prerequisites'):
                if field not in data:
                    continue
                active,legacy=[],[]
                for value in _list(data[field]):
                    old_target=model.link_target(value)
                    actual=old_target if old_target in mapping else short.get(PurePosixPath(old_target or '').name)
                    if actual and mapping[actual].startswith('01_Knowledge/'):
                        active.append(value)
                    else:
                        legacy.append(value)
                data[field]=active
                if legacy:
                    data['legacy_'+field]=list(dict.fromkeys(_list(data.get('legacy_'+field))+legacy))
                    report['unresolved_relations'].append({'path':name,'field':field,'values':legacy})
            content=model.render_note(data,record['body'])
        else:
            content=record['raw']
        if name=='总览/标签库.base':
            import yaml
            base=yaml.safe_load(content.decode('utf-8-sig'))
            base['filters']={'and':['file.ext == "md"','file.inFolder("99_System/knowledge/tags")','canonical_tag != null']}
            content=yaml.safe_dump(base,allow_unicode=True,sort_keys=False,width=1000).encode('utf-8')
        if content is not None:
            bom=b'\xef\xbb\xbf' if content.startswith(b'\xef\xbb\xbf') else b''
            rewritten=bom+change(content.decode('utf-8-sig'),name,target).encode('utf-8')
            content=None if rewritten==record['raw'] else rewritten
        operations.append({'source':name,'target':target,'content':content,'reason':'v2 migration: '+(record.get('pending') or record.get('kind') or 'original resource'),
                           'expected_sha256':sha(record['raw']) if record['raw'] is not None else None})
        if record['raw'] is None:
            operations[-1]['expected_sha256']=__import__('v2.transaction',fromlist=['file_hash']).file_hash(record['path'])
    for name,raw in new_notes.items():
        operations.append({'source':None,'target':name,'content':raw,'reason':'Academic parent MOC','expected_sha256':None})
    # Update only real moved-path references in other owned text; no project reorganization.
    for scope in ('AI','闪卡','语言','考研','每日疑惑','总览'):
        for path in _files(root,scope):
            name=path.relative_to(root).as_posix()
            if name in records or path.suffix.lower() not in ('.md','.base','.canvas'):
                continue
            raw=path.read_bytes()
            try:
                bom=b'\xef\xbb\xbf' if raw.startswith(b'\xef\xbb\xbf') else b''
                changed=bom+change(raw.decode('utf-8-sig'),name,name).encode('utf-8')
            except UnicodeError:
                continue
            if changed!=raw:
                operations.append({'source':name,'target':name,'content':changed,'reason':'Targeted moved-link repair','expected_sha256':sha(raw)})
                report['outside_link_updates'].append(name)
    report['mapping']=mapping
    report['operations']=len(operations)
    report['types']=dict(Counter(record.get('kind') or 'resource_or_pending' for record in records.values()))
    report.pop('_history',None)
    return operations,report
