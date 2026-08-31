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

landings = 1:5;

flightCount = zeros(size(landings));
refuelRate  = zeros(size(landings));

hasRefuel = ~ismissing(T.refuel_stops) & ...
            strlength(T.refuel_stops)>0;

for i = 1:numel(landings)

    idx = T.offshore_landings==landings(i);

    flightCount(i) = sum(idx);

    if flightCount(i)>0
        refuelRate(i) = 100*sum(hasRefuel(idx))/flightCount(i);
    else
        refuelRate(i) = NaN;
    end
end

figure('Color','w','Position',[210 150 760 470]);

yyaxis left

plot(landings,flightCount,'-o', ...
    'LineWidth',1.8,'MarkerSize',7);

ylabel('架次数','FontName',fontCN)

for i = 1:numel(landings)
    if flightCount(i)>0
        text(landings(i),flightCount(i)+1, ...
            sprintf('%d',flightCount(i)), ...
            'HorizontalAlignment','center', ...
            'FontName',fontEN);
    end
end

yyaxis right

plot(landings,refuelRate,'--s', ...
    'LineWidth',1.8,'MarkerSize',7);

ylabel('含加油架次比例 / %','FontName',fontCN)

xlabel('海上着陆次数','FontName',fontCN)

title('不同航线复杂度下的架次规模与加油需求', ...
    'FontName',fontCN)

xticks(1:5)
xlim([0.8 5.2])

grid on
box on

legend({'架次数','加油架次比例'}, ...
    'Location','northwest','FontName',fontCN)

ax = gca;
ax.FontName = fontEN;
ax.FontSize = 11;
ax.LineWidth = 1;