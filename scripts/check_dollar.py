import json, urllib.request, sys, re
sys.stdout.reconfigure(encoding='utf-8')

data = json.dumps({'action':'findNotes','version':6,'params':{'query':'YankiNamespace:*'}}).encode('utf-8')
ids = json.loads(urllib.request.urlopen(urllib.request.Request('http://127.0.0.1:8765',data=data)).read().decode('utf-8'))['result']

problem = []
for i in range(0, len(ids), 30):
    batch = ids[i:i+30]
    ni = json.dumps({'action':'notesInfo','version':6,'params':{'notes':batch}}).encode('utf-8')
    notes = json.loads(urllib.request.urlopen(urllib.request.Request('http://127.0.0.1:8765',data=ni)).read().decode('utf-8'))['result']
    for n in notes:
        b = n['fields']['Back']['value']
        # Find standalone $ that is inline math (not part of $$ or already converted)
        # Match $ followed by non-$ chars followed by $
        singles = re.findall(r'(?<!\$)\$([^$]+?)\$(?!\$)', b)
        if singles:
            f = n['fields']['Front']['value']
            problem.append((n['noteId'], f[:50], singles))

print(f'Total: {len(ids)}, with remaining inline $: {len(problem)}')
for nid, front, singles in problem[:8]:
    print(f'  {front[:50]}')
    for s in singles[:2]:
        print(f'    ${s}$')
