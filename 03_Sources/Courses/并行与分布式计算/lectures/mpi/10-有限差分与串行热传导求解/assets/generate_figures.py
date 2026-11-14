from pathlib import Path
import os,tempfile
os.environ['MPLCONFIGDIR']=tempfile.mkdtemp(prefix='mpi10-mpl-')
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import subprocess,csv,io,json,math
p=Path(__file__).resolve().parent
p.mkdir(exist_ok=True)
import argparse
parser=argparse.ArgumentParser()
parser.add_argument('build_dir', type=Path, help='Directory containing heat_serial and stability_demo')
b=parser.parse_args().build_dir.resolve()
plt.rcParams.update({'font.size':13,'axes.spines.top':False,'axes.spines.right':False,'pdf.fonttype':3,'svg.fonttype':'path','axes.labelcolor':'#112C43','text.color':'#112C43'})
def save(fig,name):
 for ext in ['svg','pdf','png']:fig.savefig(p/(name+'.'+ext),bbox_inches='tight',dpi=160)
 f=p/(name+'.svg');f.write_text('\n'.join(x.rstrip() for x in f.read_text().splitlines())+'\n');plt.close(fig)
records=[]
fig,axs=plt.subplots(1,2,figsize=(11,4.3));colors=['#D78738','#147F85','#112C43']
for n,c in zip([20,40,80],colors):
 proc=subprocess.run([str(b/'heat_serial'),str(n),'10'],text=True,capture_output=True,check=True)
 (p/f'solution-N{n}.csv').write_text(proc.stdout)
 rows=list(csv.DictReader(io.StringIO(proc.stdout)));x=[float(r['x_m']) for r in rows];u=[float(r['T_numeric_C']) for r in rows];e=[float(r['error_K']) for r in rows]
 meta=dict(t.split('=') for t in proc.stderr.split());meta={k:float(v) for k,v in meta.items()};meta['center_C']=u[n//2];records.append(meta)
 axs[0].plot(x,u,'o-',ms=3,color=c,label=f'N={n}');axs[1].plot(x,e,color=c,label=f'N={n}')
xs=[i/400 for i in range(401)];axs[0].plot(xs,[20+80*math.exp(-.01*math.pi**2*10)*math.sin(math.pi*x) for x in xs],'--',color='black',lw=1,label='Exact')
for ax in axs:ax.set_xlabel('Position x (m)');ax.grid(alpha=.2);ax.legend()
axs[0].set_ylabel('Temperature (C)');axs[0].set_title('t = 10 s: profiles nearly coincide');axs[1].set_ylabel('Absolute error (K)');axs[1].set_title('Error reveals the difference');fig.tight_layout();save(fig,'solution-error')
fig,ax=plt.subplots(figsize=(7.4,4.5));ns=[r['N'] for r in records];es=[r['max_error_K'] for r in records];ax.loglog(ns,es,'o-',color=colors[1],lw=2,label='Computed max error');ax.loglog(ns,[es[0]*(20/n)**2 for n in ns],'--',color=colors[0],label='N^-2 reference');ax.set(xlabel='Intervals N',ylabel='Maximum error (K)',title='Joint refinement: dt proportional to dx^2',xticks=ns);ax.set_xticklabels(['20','40','80']);ax.grid(which='both',alpha=.2);ax.legend();fig.tight_layout();save(fig,'convergence')
s=subprocess.check_output([str(b/'stability_demo')],text=True);(p/'stability.csv').write_text(s);rows=list(csv.DictReader(io.StringIO(s)))
fig,ax=plt.subplots(figsize=(8.5,4.4));steps=[int(r['step']) for r in rows]
for k,c in [('04',colors[1]),('06',colors[0])]:ax.semilogy(steps,[max(1e-15,float(r[f'amplitude_r{k}_K'])) for r in rows],label='r = 0.'+k[-1],color=c,lw=2)
ax.set(xlabel='Time-step index n (different dt for each curve)',ylabel='max |T - 20| (K)',title='N = 20, initial high-frequency amplitude = 1e-6 K');ax.grid(which='both',alpha=.2);ax.legend();fig.tight_layout();save(fig,'stability')
(p/'results.json').write_text(json.dumps({'refinement':records,'error_ratios':[es[0]/es[1],es[1]/es[2]],'stability_last':rows[-1],'mode_factors':{str(r):1-4*r*math.sin(19*math.pi/40)**2 for r in [.4,.6]}},indent=2)+'\n')
print((p/'results.json').read_text())
