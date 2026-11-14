"""Original work/ideal diagrams and plots of archived container measurements."""
from pathlib import Path
import csv, os, tempfile
os.environ.setdefault('MPLCONFIGDIR',tempfile.mkdtemp(prefix='mpi-scaling-'))
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
p=Path(__file__).resolve().parent
navy='#112C43'; teal='#147F85'; amber='#D78738'; paper='#F7FAFB'
plt.rcParams.update({'font.size':13, 'axes.spines.top':False,'axes.spines.right':False,
                     'svg.fonttype':'path','pdf.fonttype':3,'axes.labelcolor':navy,'text.color':navy})
def save(fig,name):
 for ext in ('svg','pdf','png'):
  fig.savefig(p/(name+'.'+ext),bbox_inches='tight',dpi=160)
 figpath=p/(name+'.svg'); figpath.write_text('\n'.join(x.rstrip() for x in figpath.read_text().splitlines())+'\n')
 plt.close(fig)
fig,axes=plt.subplots(1,2,figsize=(12,3.5),layout='constrained')
colors=[teal,amber,'#78669A','#507DA7']
for ax,mode in zip(axes,['Strong','Weak']):
 for y,np in enumerate([1,2,4]):
  total=16 if mode=='Strong' else 4*np
  local=total//np
  for i in range(total):
   ax.add_patch(Rectangle((i,-y),.88,.65,facecolor=colors[i//local],edgecolor='white'))
  for rank in range(np):
   ax.text((rank+.5)*local-.06,-y-.16,f'r{rank}',ha='center',va='center',color=navy,fontsize=11)
  ax.text(-.8,-y+.3,f'P={np}',ha='right',va='center')
 ax.set(xlim=(-3.4,16.5),ylim=(-2.6,1.4));ax.axis('off')
 ax.text(7,1,f'{mode} scaling',ha='center',fontsize=19,weight='bold',color=navy)
 ax.text(7,-2.55,'16 total nodes; fixed steps' if mode=='Strong' else '4 nodes per rank; fixed steps',ha='center',fontsize=12)
save(fig,'scaling-work')
fig,axes=plt.subplots(1,3,figsize=(12,3.5),layout='constrained')
xs=[1,2,4,8]
for ax,ys,title,ylabel in zip(axes,[[1/x for x in xs],xs,[1]*4],['Strong: time','Strong: speedup','Weak: time'],['T(P) / T(1)','S(P)','T(P, P W1) / T(1, W1)']):
 ax.plot(xs,ys,'o--',color=teal,lw=2); ax.set(title=title,xlabel='MPI processes P',ylabel=ylabel,xticks=xs)
 ax.grid(alpha=.18);ax.set_ylim(bottom=0)
fig.suptitle('Ideal trends only - not measured data',fontsize=15,color=navy)
save(fig,'scaling-ideal')
rows=list(csv.DictReader((p/'scaling-data/summary.csv').open()))
fig,axes=plt.subplots(1,2,figsize=(12,3.8),layout='constrained')
for ax,mode in zip(axes,['strong','weak']):
 rs=[r for r in rows if r['mode']==mode]; xs=[int(r['P']) for r in rs]
 med=[float(r['median_s'])*1000 for r in rs];lo=[float(r['min_s'])*1000 for r in rs];hi=[float(r['max_s'])*1000 for r in rs]
 ax.errorbar(xs,med,yerr=[[a-b for a,b in zip(med,lo)],[b-a for a,b in zip(med,hi)]],fmt='o-',color=teal,lw=2,capsize=5,label='Median; min-max of 5 runs')
 ideal=[med[0]/x if mode=='strong' else med[0] for x in xs]
 ax.plot(xs,ideal,'--',color=amber,lw=2,label='Ideal from P=1 median')
 ax.set(xlabel='MPI processes P',ylabel='Loop time (ms)',title='Strong: K=1600' if mode=='strong' else 'Weak: K/P=400',xticks=xs,ylim=(0,30))
 ax.grid(alpha=.18);ax.legend(fontsize=10,loc='upper left')
fig.suptitle('Container measurements: M=50,000; Release; shared local resources',fontsize=14)
save(fig,'scaling-measured')
