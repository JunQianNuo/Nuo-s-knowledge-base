const fs=require('node:fs'),path=require('node:path'),crypto=require('node:crypto');
const work=path.resolve(__dirname,'../..');
const baseline='C:/Users/Nuo/AppData/Local/Temp/claudian-dsh-compat-baseline/claudian-2.3.20';
const backup='D:/知识库/.context/claudian-dsh-compat-backup/chat-review-checkpoint';
const hash=b=>crypto.createHash('sha256').update(b).digest('hex');
fs.mkdirSync(backup,{recursive:true});
const changed=[];
function scan(rel){for(const entry of fs.readdirSync(path.join(work,rel),{withFileTypes:true})){
 const r=path.join(rel,entry.name);if(entry.isDirectory())scan(r);else if(entry.isFile()){
  const data=fs.readFileSync(path.join(work,r)),base=path.join(baseline,r);
  if(!fs.existsSync(base)||!data.equals(fs.readFileSync(base))){
   changed.push({path:r.replaceAll('\\','/'),sha256:hash(data)});
   const target=path.join(backup,'source',r);fs.mkdirSync(path.dirname(target),{recursive:true});fs.writeFileSync(target,data);
  }
 }
}}
for(const rel of ['src','tests','scripts'])scan(rel);
const names=s=>s.split(/\r?\n/).filter(l=>/^\s+● /.test(l)).map(l=>l.trim()).sort();
const original=names(fs.readFileSync('D:/知识库/.context/claudian-dsh-compat-backup/official-baseline-tests.log','utf8'));
const current=names(fs.readFileSync(path.join(__dirname,'full-tests-final.log'),'utf8'));
const added=current.filter(n=>!original.includes(n)),removed=original.filter(n=>!current.includes(n));
const report={status:'not-deployed-review-blocked',installedHash:hash(fs.readFileSync('D:/知识库/.obsidian/plugins/realclaudian/main.js')),fullJest:{failed:38,passed:7727,skipped:7,baselineFailed:38,newFailures:added,resolvedBaselineFailures:removed,failureNames:current},scripts:{passed:76,failed:0},changedSource:changed,reviewBlockers:['Live native subagents cannot use commands/list: need a root-authorized native-verified descendant route.','Cold seeded/fork sessions have no authoritative list projection: need supported cold-read contract.'],uiAccepted:false,candidateQualified:false};
fs.writeFileSync(path.join(backup,'validation.json'),JSON.stringify(report,null,2));
for(const entry of fs.readdirSync(__dirname,{withFileTypes:true}))if(entry.isFile()&&!entry.name.endsWith('.cjs')&&!entry.name.endsWith('.js'))fs.copyFileSync(path.join(__dirname,entry.name),path.join(backup,entry.name));
for(const file of ['BuildCandidate.cjs','SaveReviewCheckpoint.cjs'])fs.copyFileSync(path.join(__dirname,file),path.join(backup,file));
console.log(JSON.stringify({status:report.status,sourceFiles:changed.length,newFailureNames:added,resolvedBaselineFailureNames:removed,backup}));
