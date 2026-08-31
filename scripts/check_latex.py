import json, urllib.request, sys
sys.stdout.reconfigure(encoding='utf-8')

data = json.dumps({'action':'findNotes','version':6,'params':{'query':'deck:"最优化方法::约束优化"'}}).encode('utf-8')
ids = json.loads(urllib.request.urlopen(urllib.request.Request('http://127.0.0.1:8765',data=data)).read().decode('utf-8'))['result']

ni = json.dumps({'action':'notesInfo','version':6,'params':{'notes':ids[:1]}}).encode('utf-8')
n = json.loads(urllib.request.urlopen(urllib.request.Request('http://127.0.0.1:8765',data=ni)).read().decode('utf-8'))['result'][0]

back = n['fields']['Back']['value']
print("Has nabla:", chr(92)+"nabla" in back)
print("Has lambda:", chr(92)+"lambda" in back)
print("Has sum:", chr(92)+"sum" in back)
print()
print("Content sample:")
for line in back.split(chr(10))[:8]:
    print("  " + repr(line))
