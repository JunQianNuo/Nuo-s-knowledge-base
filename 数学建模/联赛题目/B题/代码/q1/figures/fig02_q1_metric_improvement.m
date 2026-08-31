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

M = zeros(4,height(T));

% 正值表示相对 Primary 改善，负值表示变差
M(1,:) = 100*(T.T_air(1)-T.T_air)'/T.T_air(1);
M(2,:) = 100*(T.T_pax(1)-T.T_pax)'/T.T_pax(1);
M(3,:) = 100*(T.fuel(1)-T.fuel)'/T.fuel(1);
M(4,:) = 100*(T.seat_utilization-T.seat_utilization(1))' ...
         /T.seat_utilization(1);

figure('Color','w','Position',[180 170 860 430]);

imagesc(M)
colormap(parula)

cb = colorbar;
cb.FontName = fontEN;
cb.Label.String = '相对变化率 / %';
cb.Label.FontName = fontCN;

xticks(1:height(T))
xticklabels(["Primary","LNS-1","LNS-2","LNS-3","LNS-4","Lexicographic"])

yticks(1:4)
yticklabels({'T_{air}','T_{pax}','Fuel','Utilization'})

for i = 1:size(M,1)
    for j = 1:size(M,2)
        text(j,i,sprintf('%.2f',M(i,j)), ...
            'HorizontalAlignment','center', ...
            'FontName',fontEN,'FontSize',10);
    end
end

title('各阶段相对初始方案的指标变化（正值表示改善）', ...
    'FontName',fontCN)

ax = gca;
ax.FontName = fontEN;
ax.FontSize = 11;
ax.TickLength = [0 0];