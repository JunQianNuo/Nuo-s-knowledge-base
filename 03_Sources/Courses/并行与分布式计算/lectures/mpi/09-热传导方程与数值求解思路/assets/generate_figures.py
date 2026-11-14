#!/usr/bin/env python3
"""Reproduce original lecture figures from analytic heat-equation formulas.

Requires Python 3, NumPy and Matplotlib. Run from any directory:
    python generate_figures.py
No PDE discretization or time-stepping solver is used here.
"""
from pathlib import Path
import csv
import json
import math
import os
import tempfile
os.environ.setdefault('MPLCONFIGDIR', str(Path(tempfile.gettempdir()) / 'mpi09-matplotlib-cache'))
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle, FancyArrowPatch
from matplotlib.colors import LinearSegmentedColormap, Normalize
from matplotlib import font_manager

OUT = Path(__file__).resolve().parent
NAVY, TEAL, AMBER = '#112C43', '#147F85', '#D78738'
SLATE, MINT, PAPER, GRAY = '#506574', '#E9F4F2', '#F7FAFB', '#D6E3E8'
font_names = {f.name for f in font_manager.fontManager.ttflist}
for font in ['Hiragino Sans GB', 'Noto Sans CJK SC', 'Microsoft YaHei', 'SimHei', 'PingFang SC']:
    if font in font_names:
        CHINESE = font
        break
else:
    raise RuntimeError('A Chinese font is required. Install Noto Sans CJK SC, or use a system with Hiragino Sans GB / Microsoft YaHei / SimHei / PingFang SC, then rerun this script.')
plt.rcParams.update({'font.family': [CHINESE, 'DejaVu Sans'], 'font.size': 13, 'text.color': NAVY,
                     'axes.labelcolor': NAVY, 'xtick.color': SLATE, 'ytick.color': SLATE,
                     'axes.edgecolor': GRAY, 'axes.titleweight': 'bold',
                     'axes.spines.top': False, 'axes.spines.right': False,
                     'svg.fonttype': 'path', 'pdf.fonttype': 3,
                     'savefig.facecolor': 'white', 'axes.unicode_minus': False})
L, ALPHA, BASE, AMPLITUDE = 1.0, .01, 20.0, 80.0
TIMES1 = [0., 5., 10., 20.]
TIMES2 = [0., 10., 20.]
CMAP = LinearSegmentedColormap.from_list('course_heat', ['#147F85', '#6BACAF', '#F1E3B0', '#D78738', '#AA503B'])

def t1(x, t):
    return BASE + AMPLITUDE * np.exp(-ALPHA * (np.pi / L)**2 * t) * np.sin(np.pi * np.asarray(x) / L)

def t2(x, y, t):
    return BASE + AMPLITUDE * np.exp(-2 * ALPHA * (np.pi / L)**2 * t) * np.sin(np.pi * np.asarray(x) / L) * np.sin(np.pi * np.asarray(y) / L)

def save(fig, stem):
    fig.savefig(OUT / f'{stem}.svg', bbox_inches='tight', pad_inches=.12)
    svg_path = OUT / f'{stem}.svg'
    svg_path.write_text('\n'.join(line.rstrip() for line in svg_path.read_text().splitlines()) + '\n')
    fig.savefig(OUT / f'{stem}.pdf', bbox_inches='tight', pad_inches=.12,
                metadata={'Title': stem, 'Author': 'Parallel and Distributed Computing course',
                          'Subject': 'Original figure; analytic formula sampling, not PDE simulation; Type 3 vector glyph outlines'})
    fig.savefig(OUT / f'{stem}.png', dpi=120, bbox_inches='tight', pad_inches=.12)
    plt.close(fig)

def arrow(ax, start, end, color=TEAL, scale=18, width=2.2):
    ax.add_patch(FancyArrowPatch(start, end, arrowstyle='-|>', mutation_scale=scale,
                                linewidth=width, color=color))

def rod_figure():
    fig, ax = plt.subplots(figsize=(12.4, 6.5))
    ax.set_xlim(0, 12); ax.set_ylim(0, 6.2); ax.axis('off')
    ax.text(.1, 5.95, '从热流到能量账本', fontsize=22, weight='bold', va='top')
    ax.text(.1, 5.36, '均匀细杆：侧面绝热、无内部热源；两端接触 20 °C 恒温热库', color=SLATE)
    # Color shows the initial analytic profile, not a spatial discretization.
    rodx = np.linspace(0, L, 501)
    ax.imshow(t1(rodx, 0)[None, :], cmap=CMAP, norm=Normalize(20,100),
              extent=(1.05,10.95,3.82,4.39), aspect='auto', interpolation='bilinear')
    ax.add_patch(Rectangle((1.05,3.82),9.9,.57,fill=False,edgecolor=NAVY,linewidth=1.2))
    ax.add_patch(Rectangle((.78,3.52),.27,1.17,facecolor=MINT,edgecolor=TEAL,linewidth=1.5))
    ax.add_patch(Rectangle((10.95,3.52),.27,1.17,facecolor=MINT,edgecolor=TEAL,linewidth=1.5))
    ax.text(.9,3.16,'x = 0\n20 °C',ha='center',va='top')
    ax.text(11.1,3.16,'x = L\n20 °C',ha='center',va='top')
    ax.text(6.,4.63,'初始中心 100 °C',ha='center',color=AMBER,weight='bold')
    arrow(ax,(5.1,3.46),(3.6,3.46),AMBER)
    arrow(ax,(6.9,3.46),(8.4,3.46),AMBER)
    ax.text(6.,3.12,'热由中心高温区流向两端低温区',ha='center',color=SLATE)
    # A finite control volume. The balance below is a rate equality, not a point approximation.
    box=FancyBboxPatch((4.7,1.2),2.6,1.15,boxstyle='round,pad=0.08',facecolor=MINT,edgecolor=TEAL,linewidth=1.6)
    ax.add_patch(box)
    ax.text(6.,1.8,'固定小段\n横截面 A',ha='center',va='center',fontsize=15,weight='bold')
    arrow(ax,(1.5,1.78),(4.5,1.78),TEAL)
    arrow(ax,(7.5,1.78),(10.5,1.78),AMBER)
    ax.text(2.9,2.14,'左端：A q(x,t)',ha='center',color=TEAL)
    ax.text(9.1,2.14,'右端：A q(x+Δx,t)',ha='center',color=AMBER)
    ax.text(4.7,.91,'x',ha='center',color=SLATE)
    ax.text(7.3,.91,'x + Δx',ha='center',color=SLATE)
    ax.text(6.,.34,'积累速率 = 流入功率 - 流出功率',ha='center',fontsize=17,weight='bold')
    ax.text(6.,-.05,'小段图中的 q 以 +x 为正方向；q 可为正或负，功率单位为 W。',ha='center',color=SLATE,fontsize=11)
    save(fig,'rod-energy-balance')

def curvature_figure():
    fig, axs=plt.subplots(1,3,figsize=(12.4,4.6))
    x=np.linspace(0,1,301)
    ys=[100-80*x,20+80*np.sin(np.pi*x),80-60*np.sin(np.pi*x)]
    titles=['线性剖面：热流非零，局部不积热','峰顶：斜率为零，仍会降温','谷底：斜率为零，仍会升温']
    bottom=[r'$T_x<0,\quad T_{xx}=0\ \Rightarrow\ T_t=0$',
            r'$T_x=0,\quad T_{xx}<0\ \Rightarrow\ T_t<0$',
            r'$T_x=0,\quad T_{xx}>0\ \Rightarrow\ T_t>0$']
    colors=[TEAL,AMBER,NAVY]
    for ax,y,title,desc,c in zip(axs,ys,titles,bottom,colors):
        ax.plot(x,y,color=c,linewidth=3)
        ax.scatter([.5],[np.interp(.5,x,y)],color=c,s=55,zorder=3)
        ax.axvline(.5,color=GRAY,linestyle='--')
        ax.set(xlim=(0,1),ylim=(10,110),xticks=[0,.5,1],yticks=[20,60,100],xlabel='位置 x（m）')
        ax.set_title(title,fontsize=12,pad=12)
        ax.grid(axis='y',color=GRAY,alpha=.5)
        ax.text(.5,-.35,desc,transform=ax.transAxes,ha='center',fontsize=12,color=c)
    axs[0].set_ylabel('温度 T（°C）')
    fig.suptitle('温度梯度决定热流方向，温度曲率决定局部升降',fontsize=19,weight='bold',y=1.04)
    fig.text(.5,-.02,'三个独立剖面均假定 α>0、无热源；符号判断取 x=0.5 m。',ha='center',color=SLATE,fontsize=11)
    fig.subplots_adjust(wspace=.30,bottom=.27,top=.84)
    save(fig,'slope-vs-curvature')

def line_figure():
    x=np.linspace(0,1,401)
    fig,ax=plt.subplots(figsize=(10.2,5.5))
    for t,c,ls in zip(TIMES1,[AMBER,TEAL,NAVY,'#799296'],['-','-','-','--']):
        ax.plot(x,t1(x,t),label=f't = {t:g} s',color=c,lw=2.7,ls=ls)
    ax.set(xlim=(0,1),ylim=(16,104),xticks=np.arange(0,1.01,.2),yticks=[20,40,60,80,100],xlabel='位置 x（m）',ylabel='温度 T（°C）')
    ax.grid(color=GRAY,alpha=.65)
    ax.legend(frameon=False,loc='upper right',ncols=2)
    ax.set_title('细杆的正弦模态随时间衰减',fontsize=20,pad=21)
    ax.text(.5,1.025,'L = 1 m，α = 0.01 m²/s；两端始终保持 20 °C',transform=ax.transAxes,ha='center',color=SLATE,fontsize=12)
    ax.scatter([.5],[t1(.5,10)],color=NAVY,s=40,zorder=4)
    ax.annotate(f't = 10 s：中心 {t1(.5,10):.4f} °C',xy=(.5,t1(.5,10)),xytext=(.5,24),color=NAVY,
                fontsize=12,arrowprops={'arrowstyle':'->','color':NAVY},ha='center')
    fig.text(.5,-.015,'曲线由解析公式直接采样；α 是教学假设参数，非特定材料测量值。',ha='center',color=SLATE,fontsize=11)
    fig.tight_layout()
    save(fig,'heat-line-profiles')

def plate_figure():
    x=np.linspace(0,1,201);X,Y=np.meshgrid(x,x)
    fig,axs=plt.subplots(1,3,figsize=(12.4,4.8))
    norm=Normalize(20,100)
    for ax,t in zip(axs,TIMES2):
        Z=t2(X,Y,t)
        image=ax.imshow(Z,origin='lower',extent=(0,1,0,1),cmap=CMAP,norm=norm,interpolation='bilinear')
        ax.set(xlabel='x（m）',xticks=[0,.5,1],yticks=[0,.5,1])
        ax.set_title(f't = {t:g} s\n中心 {t2(.5,.5,t):.4f} °C',fontsize=13,pad=9)
        ax.set_aspect('equal')
    axs[0].set_ylabel('y（m）')
    fig.suptitle('二维方板的解析温度场：四边始终保持 20 °C',fontsize=19,weight='bold',y=1.02)
    fig.subplots_adjust(wspace=.27,bottom=.30,top=.78)
    cax=fig.add_axes([.30,.14,.40,.035])
    cbar=fig.colorbar(image,cax=cax,orientation='horizontal',ticks=[20,40,60,80,100])
    cbar.set_label('所有时刻共用色标：温度 T（°C）',fontsize=11)
    fig.text(.5,.015,'L = 1 m，α = 0.01 m²/s。图为解析公式采样，不是差分求解器输出。',ha='center',color=SLATE,fontsize=11)
    save(fig,'heat-plate-fields')

def write_data():
    with (OUT/'heat-line-reference.csv').open('w',newline='') as f:
        w=csv.writer(f, lineterminator='\n');w.writerow(['x_m','time_s','temperature_C'])
        for t in TIMES1:
            for x in np.linspace(0,1,101):w.writerow([f'{x:.6f}',f'{t:.1f}',f'{t1(x,t):.12f}'])
    with (OUT/'heat-plate-reference.csv').open('w',newline='') as f:
        w=csv.writer(f, lineterminator='\n');w.writerow(['x_m','y_m','time_s','temperature_C'])
        for t in TIMES2:
            for y in np.linspace(0,1,21):
                for x in np.linspace(0,1,21):w.writerow([f'{x:.6f}',f'{y:.6f}',f'{t:.1f}',f'{t2(x,y,t):.12f}'])
    params={'L_m':L,'alpha_m2_per_s':ALPHA,'base_C':BASE,'amplitude_K':AMPLITUDE,'time_1d_s':TIMES1,'time_2d_s':TIMES2,'tau_1d_s':L*L/(ALPHA*math.pi**2),'tau_2d_s':L*L/(2*ALPHA*math.pi**2),'centre_1d_10s_C':float(t1(.5,10)),'centre_2d_10s_C':float(t2(.5,.5,10)),'kind':'Analytic formula samples, not numerical time stepping','font':CHINESE}
    (OUT/'figure-parameters.json').write_text(json.dumps(params,ensure_ascii=False,indent=2)+'\n')

if __name__=='__main__':
    rod_figure();curvature_figure();line_figure();plate_figure();write_data()
    print('Generated four SVG/PDF/PNG figures, two CSV tables and parameter record in',OUT)
