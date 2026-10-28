"""Contextual topics rule: reuse Schema and link resolution, require explicit role:moc."""
from __future__ import annotations
import sys
sys.dont_write_bytecode=True
import hashlib
import link_validator as links
v=links.v

def is_moc(raw, path, system):
    if v.is_system_path(path, system):return False
    try:
        metadata=v.parse_frontmatter(raw) or {}
        return metadata.get('role')=='moc' and v.validate_note(raw,path,system)['classification']=='valid'
    except (UnicodeError, ValueError, v.yaml.YAMLError, RecursionError):return False

def applies(raw, path, system):
    if not path.casefold().endswith('.md') or v.is_system_path(path,system):return False
    metadata=v.parse_frontmatter(raw) or {}
    return ('schema_version' in metadata or metadata.get('type') in v.ATOMIC_TYPES or metadata.get('role')=='moc') and bool(metadata.get('topics'))

def audit(raw, source, index, system, rows=None):
    report={'policy':'topics_require_explicit_moc','enforced':False,'ok':True,'targets':[],'errors':[]}
    try:
        if not applies(raw,source,system):return report
    except (UnicodeError, ValueError, v.yaml.YAMLError, RecursionError):return report
    report['enforced']=True
    if v.validate_note(raw,source,system)['classification']!='valid':
        report['ok']=False;report['errors'].append({'code':'invalid_v1_metadata','field':'topics'});return report
    if rows is None:
        metadata=v.parse_frontmatter(raw)
        scoped=('---\n'+v.yaml.safe_dump({'type':'concept','topics':metadata['topics']},allow_unicode=True)+'---\n').encode()
        rows=links.audit_links(scoped,source,index,system)
    for row in rows:
        if not (row.get('field') or '').startswith('topics/'):continue
        item={'field':row['field'],'raw':row['raw'],'link_status':row['status'],'candidates':row['candidates'],'basis':row['basis']}
        code=None
        if row['status']!='resolved' or len(row['candidates'])!=1:code='topic_'+row['status']
        else:
            target=row['candidates'][0];path=index.root/target
            if not target.casefold().endswith('.md') or v.is_system_path(target,system):code='topic_system_or_non_note'
            elif links.protected_reason(index.root,path):code='topic_protected_target'
            else:
                try:
                    target_raw=path.read_bytes();item['target_sha256']=hashlib.sha256(target_raw).hexdigest()
                    if not is_moc(target_raw,target,system):code='topic_target_requires_role_moc'
                except (OSError,UnicodeError,ValueError,v.yaml.YAMLError,RecursionError):code='topic_target_unchecked'
        item['eligible']=code is None;report['targets'].append(item)
        if code:report['errors'].append({'code':code,'field':row['field'],'candidates':row['candidates'],'basis':row['basis']})
    report['ok']=not report['errors']
    return report

def require(raw, source, index, system):
    result=audit(raw,source,index,system)
    if not result['ok']:raise ValueError('Topic policy: '+str(result['errors']))
    return result
