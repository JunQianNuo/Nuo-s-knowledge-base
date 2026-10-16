const fs=require('node:fs'),path=require('node:path'),crypto=require('node:crypto'),acorn=require('acorn'),scope=require('eslint-scope');
const root=path.resolve(__dirname,'../..');
const hash=s=>crypto.createHash('sha256').update(s).digest('hex');
function norm(n,parent,key){
 if(Array.isArray(n))return n.map(x=>norm(x,parent,key));
 if(!n||typeof n!=='object')return n;
 if(n.type==='Identifier'){
  const external=(parent?.type==='MemberExpression'&&key==='property'&&!parent.computed)||(['Property','MethodDefinition','PropertyDefinition'].includes(parent?.type)&&key==='key'&&!parent.computed);
  return {type:n.type,name:external?n.name:'$'};
 }
 const o={};for(const [k,v]of Object.entries(n))if(!['start','end','range','raw'].includes(k))o[k]=norm(v,n,k);return o;
}
function load(file){
 const code=fs.readFileSync(file,'utf8'),ast=acorn.parse(code,{ecmaVersion:'latest',ranges:true});
 const sm=scope.analyze(ast,{ecmaVersion:2022,sourceType:'script',optimistic:true,ignoreEval:true});
 const defs=sm.globalScope.variables.filter(v=>v.defs.length===1&&['Variable','FunctionName'].includes(v.defs[0].type)).map(v=>{
  const d=v.defs[0],node=d.type==='Variable'?d.node.init:d.node;
  return node?{name:v.name,node,id:d.name,variable:v,fp:hash(JSON.stringify(norm(node)))}:null;
 }).filter(Boolean).sort((a,b)=>a.node.start-b.node.start);
 return {code,ast,sm,defs};
}
const old=load('D:/知识库/.obsidian/plugins/realclaudian/main.js'),fresh=load(path.join(root,'main.js'));
const oldByFp=new Map();for(const d of old.defs){const arr=oldByFp.get(d.fp)||[];arr.push(d);oldByFp.set(d.fp,arr);}
const pairs=[],mapping=new Map();let prev=-1;
for(const d of fresh.defs){const candidates=oldByFp.get(d.fp);if(candidates?.length===1){const o=candidates[0],i=old.defs.indexOf(o);if(i>prev){pairs.push([o,d]);mapping.set(d.name,o.name);prev=i;}}}
let oi=-1,ni=-1;const gaps=[];
for(const [o,n]of [...pairs, [null,null]]){
 const oe=o?old.defs.indexOf(o):old.defs.length,ne=n?fresh.defs.indexOf(n):fresh.defs.length;
 const os=old.defs.slice(oi+1,oe),ns=fresh.defs.slice(ni+1,ne);
 // Repeated, unchanged definitions align by local position; mismatched chunks remain explicit.
 if(os.length===ns.length&&os.every((v,i)=>v.fp===ns[i].fp)){for(let i=0;i<os.length;i++){mapping.set(ns[i].name,os[i].name);pairs.push;}}
 else if(os.length||ns.length)gaps.push({old:os.map(d=>({name:d.name,len:d.node.end-d.node.start,text:old.code.slice(d.node.start,d.node.start+140)})),new:ns.map(d=>({name:d.name,len:d.node.end-d.node.start,text:fresh.code.slice(d.node.start,d.node.start+140)}))});
 oi=oe;ni=ne;
}
fs.writeFileSync(path.join(__dirname,'artifact-gaps.json'),JSON.stringify(gaps,null,2));
console.log({oldDefs:old.defs.length,newDefs:fresh.defs.length,mapped:mapping.size,gaps:gaps.length});
const explicit={qC:'GC',HCe:'OCe',D6:'T6',Mw:'Aw',H6:'O6',Oi:'lr',Um:'Bm',KD:'jD',bd:'Sd',Ro:'Ro',Dw:'Ow',ju:'Wu',t4:'Q6',_w:'Lw',Nw:'_w'};
for(const [n,o]of Object.entries(explicit))mapping.set(n,o);
const added=['GC','F3','H3','B3','U3','Sd'];
for(const [i,n]of added.entries())mapping.set(n,`__claudianDshChatCompat${i}`);
const missing=fresh.defs.filter(d=>!mapping.has(d.name));
if(missing.length)throw new Error('Unmapped globals: '+missing.map(d=>d.name).join(','));
const oldByName=new Map(old.defs.map(d=>[d.name,d]));
const edits=[];
const refs=fresh.sm.scopes.flatMap(s=>s.references).filter(r=>r.resolved?.scope===fresh.sm.globalScope);
function transform(d){
 const changes=new Map();
 for(const r of refs)if(r.identifier.start>=d.node.start&&r.identifier.end<=d.node.end){
  const name=mapping.get(r.identifier.name);
  if(!name)throw new Error('Unmapped referenced global '+r.identifier.name);
  changes.set(r.identifier.start,{start:r.identifier.start,end:r.identifier.end,text:name});
 }
 if(d.node.type==='FunctionDeclaration')changes.set(d.id.start,{start:d.id.start,end:d.id.end,text:mapping.get(d.name)});
 let text=fresh.code.slice(d.node.start,d.node.end);
 for(const c of [...changes.values()].sort((a,b)=>b.start-a.start))text=text.slice(0,c.start-d.node.start)+c.text+text.slice(c.end-d.node.start);
 return text;
}
for(const d of fresh.defs){
 if(added.includes(d.name))continue;
 const o=oldByName.get(mapping.get(d.name));
 if(!o)throw new Error('Missing original '+d.name);
 if(d.fp!==o.fp)edits.push({start:o.node.start,end:o.node.end,text:transform(d),oldName:o.name,newName:d.name,original:old.code.slice(o.node.start,o.node.end)});
}
let candidate=old.code;
for(const e of [...edits].sort((a,b)=>b.start-a.start))candidate=candidate.slice(0,e.start)+e.text+candidate.slice(e.end);
const mainLength=candidate.length;
candidate+='\n// Claudian scoped DeepSeek protocol compatibility dependencies.\n'+added.map(name=>{
 const d=fresh.defs.find(d=>d.name===name),text=transform(d);
 return d.node.type==='FunctionDeclaration'?text:`var ${mapping.get(name)}=${text};`;
}).join('\n')+'\n';
acorn.parse(candidate,{ecmaVersion:'latest'});
// Reverse the exact changed intervals and appended dependencies to prove untouched bytes.
let restored=candidate.slice(0,mainLength),offset=0;
const positions=edits.sort((a,b)=>a.start-b.start).map(e=>{const pos=e.start+offset;offset+=e.text.length-(e.end-e.start);return {...e,pos};});
for(const e of [...positions].reverse())restored=restored.slice(0,e.pos)+e.original+restored.slice(e.pos+e.text.length);
if(restored!==old.code)throw new Error('Unrelated bytes changed');
const report={oldHash:hash(old.code),builtHash:hash(fresh.code),candidateHash:hash(candidate),unrelatedBytesPreserved:true,changed:edits.map(e=>({oldName:e.oldName,newName:e.newName,oldBytes:e.end-e.start,newBytes:e.text.length})),added,mapping:Object.fromEntries(mapping)};
fs.writeFileSync(path.join(__dirname,'candidate-main.js'),candidate);
fs.writeFileSync(path.join(__dirname,'candidate-artifact.json'),JSON.stringify(report,null,2));
console.log(JSON.stringify({...report,mapping:undefined},null,2));
