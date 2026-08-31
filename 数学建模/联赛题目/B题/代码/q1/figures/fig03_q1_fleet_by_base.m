clear; clc; close all

fontCN = 'SimSun';
fontEN = 'Times New Roman';

p = fileparts(mfilename('fullpath'));
if isfolder(fullfile(p,'outputs'))
    outDir = fullfile(p,'outputs');
else
    outDir = fullfile(fileparts(p),'outputs');
end

T = readtable(fullfile(outDir,'q1-flight-plan.csv'), ...
    'TextType','string','VariableNamingRule','preserve');

bases = ["A01","A02","A03"];
types = ["T1","T2","T3"];

N = zeros(numel(bases),numel(types));

for i = 1:numel(bases)
    for j = 1:numel(types)
        N(i,j) = sum(T.base_airport==bases(i) & ...
                     T.aircraft_type==types(j));
    end
end

figure('Color','w','Position',[220 160 720 470]);

b = bar(N,'stacked','BarWidth',0.62);

b(1).FaceColor = [0.35 0.65 0.85];
b(2).FaceColor = [0.95 0.65 0.25];
b(3).FaceColor = [0.35 0.70 0.45];

xticks(1:numel(bases))
xticklabels(bases)

ylabel('架次数','FontName',fontCN)
title('不同基地机场的机型架次组成','FontName',fontCN)

% 显式指定顺序，避免 MATLAB 自动反转
legend([b(1),b(2),b(3)],{'T1','T2','T3'}, ...
    'Location','northwest','FontName',fontEN);

grid on
box on

total = sum(N,2);

for i = 1:numel(total)
    text(i,total(i)+0.8,sprintf('%d',total(i)), ...
        'HorizontalAlignment','center', ...
        'FontName',fontEN);
end

ax = gca;
ax.FontName = fontEN;
ax.FontSize = 11;
ax.LineWidth = 1;