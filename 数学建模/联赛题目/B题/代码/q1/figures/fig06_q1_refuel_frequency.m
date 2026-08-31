clear; clc; close all

fontCN = 'SimSun';
fontEN = 'Times New Roman';

p = fileparts(mfilename('fullpath'));
if isfolder(fullfile(p,'outputs'))
    outDir = fullfile(p,'outputs');
else
    outDir = fullfile(fileparts(p),'outputs');
end

T = readtable(fullfile(outDir,'q1-routes.csv'), ...
    'TextType','string','VariableNamingRule','preserve');

sites = ["F006","F011","F018","F024", ...
         "F031","F038","F044","F050"];

count = zeros(size(sites));

for i = 1:numel(sites)
    count(i) = sum(T.facility_id==sites(i) & T.refuel==1);
end

figure('Color','w','Position',[210 170 760 440]);

stem(1:numel(sites),count, ...
    'filled','LineWidth',1.6,'MarkerSize',7);

xticks(1:numel(sites))
xticklabels(sites)

ylabel('实际加油次数','FontName',fontCN)
title('各允许加油设施的实际使用频率','FontName',fontCN)

grid on
box on

for i = 1:numel(count)
    text(i,count(i)+0.25,sprintf('%d',count(i)), ...
        'HorizontalAlignment','center','FontName',fontEN);
end

ax = gca;
ax.FontName = fontEN;
ax.FontSize = 11;
ax.LineWidth = 1;