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
facilities = "F" + compose("%03d",1:52);

% M(i,j): 基地 i 向设施 j 运送的人数
M = zeros(numel(bases),numel(facilities));

for i = 1:height(T)

    s = T.("load")(i);

    if ismissing(s) || strlength(s)==0
        continue
    end

    items = split(s,"|");
    b = find(bases == T.base_airport(i),1);

    for j = 1:numel(items)

        f = split(items(j),":");

        n = str2double(f(2));   % 人数
        facility = f(3);        % 设施编号

        k = find(facilities == facility,1);

        if ~isempty(b) && ~isempty(k)
            M(b,k) = M(b,k) + n;
        end
    end
end

% 校验：图中统计的人数必须等于最终方案运输总人数
assert(sum(M(:)) == sum(T.passengers), ...
    '运输人数统计与 q1-flight-plan.csv 不一致');

figure('Color','w','Position',[60 140 1200 460]);

b = bar(M','stacked','BarWidth',0.85);

b(1).FaceColor = [0.30 0.60 0.85];   % A01
b(2).FaceColor = [0.92 0.60 0.20];   % A02
b(3).FaceColor = [0.40 0.72 0.42];   % A03

xlabel('海上设施','FontName',fontCN)
ylabel('运输人数','FontName',fontCN)
title('最终方案中各海上设施的人员运输构成', ...
    'FontName',fontCN)

% 横轴标签隔4个显示一个
tick = 1:4:52;
xticks(tick)
xticklabels(facilities(tick))

legend([b(1),b(2),b(3)], {'A01','A02','A03'}, ...
    'Location','northeastoutside', ...
    'FontName',fontEN)

grid on
box on

ax = gca;
ax.FontName = fontEN;
ax.FontSize = 10;
ax.LineWidth = 1;
xlim([0.5, 52.5])

% === 统一显示每个设施的总人数 ===
totalPerFacility = sum(M,1);

for i = 1:numel(totalPerFacility)
    if totalPerFacility(i) > 0
        text(i, totalPerFacility(i)+0.8, sprintf('%d', totalPerFacility(i)), ...
            'HorizontalAlignment','center', ...
            'VerticalAlignment','bottom', ...
            'FontName',fontEN, ...
            'FontSize',9);
    end
end