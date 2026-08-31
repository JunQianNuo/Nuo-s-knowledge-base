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

capacity = zeros(height(T),1);

capacity(T.aircraft_type=="T1") = 12;
capacity(T.aircraft_type=="T2") = 16;
capacity(T.aircraft_type=="T3") = 19;

emptySeats = capacity - T.passengers;

types = ["T2","T3"];
maxEmpty = max(emptySeats);
x = 0:maxEmpty;

C = zeros(numel(types),numel(x));

for i = 1:numel(types)
    e = emptySeats(T.aircraft_type==types(i));

    for j = 1:numel(x)
        C(i,j) = sum(e==x(j));
    end
end

figure('Color','w','Position',[220 160 760 470]);
hold on

plot(x,C(1,:),'-o', ...
    'LineWidth',1.8,'MarkerSize',7);

plot(x,C(2,:),'-s', ...
    'LineWidth',1.8,'MarkerSize',7);

for i = 1:numel(types)
    for j = 1:numel(x)
        if C(i,j)>0
            text(x(j),C(i,j)+0.7,sprintf('%d',C(i,j)), ...
                'HorizontalAlignment','center', ...
                'FontName',fontEN,'FontSize',10);
        end
    end
end

xlabel('单架次空余座位数','FontName',fontCN)
ylabel('架次数','FontName',fontCN)

title('不同机型架次的空余座位分布', ...
    'FontName',fontCN)

legend({'T2','T3'}, ...
    'Location','northeast','FontName',fontEN)

xticks(x)

grid on
box on

ax = gca;
ax.FontName = fontEN;
ax.FontSize = 11;
ax.LineWidth = 1;