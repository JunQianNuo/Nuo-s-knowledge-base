"""Rebuild original diagrams and plots from the archived MPI CSV files."""
from pathlib import Path
import csv, html, json, os, tempfile
os.environ.setdefault('MPLCONFIGDIR',tempfile.mkdtemp(prefix='mpi11-mpl-'))
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.ticker import NullFormatter
p=Path(__file__).resolve().parent
navy='#112C43';teal='#147F85';amber='#D78738';slate='#506574';mint='#E9F4F2';paper='#F7FAFB'
def start(h):return [f'<svg xmlns="http://www.w3.org/2000/svg" width="1100" height="{h}" viewBox="0 0 1100 {h}">',f'<rect width="1100" height="{h}" fill="white"/>','<defs><marker id="arrow" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 Z" fill="'+slate+'"/></marker></defs>']
def text(s,x,y,t,size=24,color=navy,anchor='middle'):
 s.append(f'<text x="{x}" y="{y}" fill="{color}" font-size="{size}" text-anchor="{anchor}" font-family="Arial, PingFang SC, sans-serif">{html.escape(str(t))}</text>')
def box(s,x,y,w,h,t,fill=mint,stroke=teal):
 s.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="{fill}" stroke="{stroke}" stroke-width="2"/>');text(s,x+w/2,y+h/2+8,t)
def arrow(s,x1,y1,x2,y2):s.append(f'<path d="M{x1},{y1} L{x2},{y2}" stroke="{slate}" stroke-width="2.5" fill="none" marker-end="url(#arrow)"/>')
def save_svg(s,name):s.append('</svg>');(p/name).write_text('\n'.join(s)+'\n')
s=start(310);text(s,550,38,'N = 11：10 个内部节点分给 3 个 rank',30)
for i in range(12):
 color=paper if i in [0,11] else [mint,'#EDF1F6','#FBF0E2'][0 if i<=4 else 1 if i<=7 else 2]
 box(s,36+i*86,100,76,58,str(i),color)
text(s,200,85,'全局 i',20)
text(s,74,200,'恒温端点',18);text(s,1020,200,'恒温端点',18)
for x,t in [(288,'rank 0：i = 1..4'),(590,'rank 1：i = 5..7'),(847,'rank 2：i = 8..10')]:text(s,x,225,t,24)
text(s,550,278,'每个内部节点只有一个负责更新的进程；端点不套用内部差分公式',22)
save_svg(s,'domain-partition.svg')
s=start(420);text(s,550,35,'幽灵值是邻居拥有值的副本',30)
# Separate rows keep ownership and reception clear.
for row,(rank,vals,m) in enumerate([(0,['20','101','102','103','104','105'],4),(1,['104','105','106','107','108'],3),(2,['107','108','109','110','20'],3)]):
 y=75+row*95;text(s,85,y+35,'rank '+str(rank),24)
 for j,val in enumerate(vals):box(s,180+j*135,y,110,55,val,paper if j in [0,m+1] else mint,amber if j in [0,m+1] else teal)
text(s,550,382,'青色：拥有值　橙色边框：ghost / 物理边界；值 = 100 + 全局 i',22)
save_svg(s,'halo-values.svg')
s=start(300);text(s,550,40,'每个时间步：先准备旧层邻居，再更新拥有值',30)
for x,w,t in [(35,210,'设置物理边界'),(290,210,'交换旧层 halo'),(545,210,'计算 next[1..m]'),(800,260,'交换 old / next')]:box(s,x,110,w,65,t)
for a,b in [(245,290),(500,545),(755,800)]:arrow(s,a+4,142,b-6,142)
text(s,550,225,'所有更新只读同一旧层；每步不额外加入全局 Barrier',24)
text(s,550,267,'下一步重复上述顺序；ghost 不作为额外未知量更新',22)
save_svg(s,'time-step.svg')
s=start(340);text(s,550,37,'Gatherv：只汇总拥有值，接收基址为 global + 1',28)
for x,w,t in [(110,290,'rank 0：4 个值'),(445,220,'rank 1：3 个值'),(710,220,'rank 2：3 个值')]:box(s,x,85,w,60,t)
for i in range(12):box(s,36+86*i,205,76,48,str(i),paper if i in [0,11] else mint)
for x1,x2 in [(255,160),(555,504),(820,762)]:arrow(s,x1,148,x2,200)
text(s,550,290,'counts = [4, 3, 3]　　displs = [0, 4, 7]（double 元素间隔）',23)
text(s,550,325,'global[0] 与 global[11] 由 root 设置为 20；ghost 不发送',22)
save_svg(s,'gatherv-layout.svg')
plt.rcParams.update({'font.size':13,'axes.spines.top':False,'axes.spines.right':False,'svg.fonttype':'path','pdf.fonttype':3,'axes.labelcolor':navy,'text.color':navy})
def rows(n,np):return list(csv.DictReader((p/f'solution-N{n}-P{np}.csv').open()))
def save(fig,name):
 for ext in ['svg','pdf','png']:fig.savefig(p/(name+'.'+ext),bbox_inches='tight',dpi=160)
 f=p/(name+'.svg');f.write_text('\n'.join(x.rstrip() for x in f.read_text().splitlines())+'\n');plt.close(fig)
r=rows(20,3);one=rows(20,1);x=[float(a['x_m']) for a in r];u=[float(a['T_numeric_C']) for a in r]
fig,ax=plt.subplots(figsize=(10,4.4));ax.plot(x,[float(a['T_numeric_C']) for a in one],color=navy,lw=1.5,label='MPI P=1 baseline')
for rank,(start,count,color) in enumerate([(1,7,teal),(8,6,amber),(14,6,'#7B6997')]):
 ax.scatter(x[start:start+count],u[start:start+count],s=47,color=color,label=f'P=3: rank {rank}',zorder=3)
ax.scatter([0,1],[20,20],marker='s',color=navy,s=35,label='Physical endpoints',zorder=4)
ax.set(xlabel='Position x (m)',ylabel='Temperature (degrees C)',title='N=20, t=10 s: distributed nodes form one temperature field')
ax.grid(alpha=.2);ax.legend(loc='upper right',fontsize=10);fig.tight_layout();save(fig,'parallel-profile')
ns=[20,40,80];err=[max(float(a['error_K']) for a in rows(n,3)) for n in ns]
fig,ax=plt.subplots(figsize=(8.4,4.5));ax.loglog(ns,err,'o-',lw=2,color=teal,label='MPI P=3: max error')
ax.loglog(ns,[err[0]*(20/n)**2 for n in ns],'--',color=amber,label='N^-2 reference')
ax.set(xlabel='Intervals N',ylabel='Maximum error (K)',title='Same refinement trend as the serial solver',xticks=ns)
ax.set_xticklabels(['20','40','80']);ax.xaxis.set_minor_formatter(NullFormatter());ax.grid(which='both',alpha=.2);ax.legend();fig.tight_layout();save(fig,'refinement')
print('4 original diagrams and 2 scientific plots generated')
