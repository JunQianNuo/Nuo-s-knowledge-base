clear; clc; close all

fontCN = 'SimSun';
fontEN = 'Times New Roman';

p = fileparts(mfilename('fullpath'));
if isfolder(fullfile(p,'outputs'))
    outDir = fullfile(p,'outputs');
else
    outDir = fullfile(fileparts(p),'outputs');
end

T = readtable(fullfile(outDir,'q1-history.csv'), ...
    'TextType','string','VariableNamingRule','preserve');

x = 1:height(T);

figure('Color','w','Position',[200 160 820 470]);
hold on

plot(x,T.T_air,'-o','LineWidth',1.8,'MarkerSize',6);
plot(x,T.cp_sat_bound,'--s','LineWidth',1.5,'MarkerSize',5);
plot(x,T.lp_bound,':','LineWidth',1.8);

grid on
box on

xticks(x)
xticklabels(["Primary","LNS-1","LNS-2","LNS-3","LNS-4","Lexicographic"])

ylabel('总飞机使用时间 / min','FontName',fontCN)
title('问题一求解过程及下界变化','FontName',fontCN)

legend({'Incumbent','CP-SAT bound','LP bound'}, ...
    'Location','best','FontName',fontEN)

ax = gca;
ax.FontName = fontEN;
ax.FontSize = 11;
ax.LineWidth = 1;

text(x(end),T.T_air(end),sprintf('  %d',T.T_air(end)), ...
    'FontName',fontEN,'FontSize',11,'VerticalAlignment','bottom');