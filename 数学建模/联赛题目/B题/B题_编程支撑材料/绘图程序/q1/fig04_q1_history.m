clear; clc;

root = projectRoot();
outDir = fullfile(root, '代码', 'q1', 'outputs');

summaryFile = fullfile(outDir, 'q1-summary.json');
historyFile = fullfile(outDir, 'q1-history.csv');

if ~isfile(summaryFile)
    error('找不到文件：%s', summaryFile);
end

if ~isfile(historyFile)
    error('找不到文件：%s', historyFile);
end

S = jsondecode(fileread(summaryFile));
H = readtable(historyFile, 'TextType', 'string');

set(groot, ...
    'defaultAxesFontName', 'Times New Roman', ...
    'defaultTextFontName', 'Times New Roman');

%% 数据
oldBaseline = 16703;      % 图表规划表中的上一版正式基线
greedy = S.greedy_T_air;
lpBound = S.lp_lower_bound;

Tair = [oldBaseline; greedy; H.T_air];

labels = { ...
    'V2.0', ...
    'Greedy', ...
    'Primary', ...
    'LNS-1', ...
    'LNS-2', ...
    'LNS-3', ...
    'LNS-4', ...
    'Lex'};

x = 1:numel(Tair);

improvement = 100 * ...
    (oldBaseline - Tair(end)) / oldBaseline;

lpDifference = 100 * ...
    (Tair(end) - lpBound) / Tair(end);

%% 绘图
figure('Color', 'w', ...
    'Position', [120 100 1000 560]);

ax = axes;
hold(ax, 'on');

stairs(ax, x, Tair, '-o', ...
    'LineWidth', 1.8, ...
    'MarkerSize', 7, ...
    'MarkerFaceColor', 'w');

yline(ax, lpBound, '--', ...
    sprintf('LP bound = %.1f', lpBound), ...
    'LineWidth', 1.4, ...
    'FontName', 'Times New Roman', ...
    'LabelHorizontalAlignment', 'left');

%% 数值标签
for i = 1:numel(Tair)

    text(ax, x(i), Tair(i) + 55, ...
        sprintf('%.0f', Tair(i)), ...
        'HorizontalAlignment', 'center', ...
        'VerticalAlignment', 'bottom', ...
        'FontName', 'Times New Roman', ...
        'FontSize', 10);
end

%% 最终结果说明
text(ax, 0.98, 0.92, ...
    sprintf('Improvement vs V2.0 = %.2f%%', improvement), ...
    'Units', 'normalized', ...
    'HorizontalAlignment', 'right', ...
    'FontName', 'Times New Roman', ...
    'FontSize', 11);

text(ax, 0.98, 0.85, ...
    sprintf('Difference vs LP bound = %.2f%%', lpDifference), ...
    'Units', 'normalized', ...
    'HorizontalAlignment', 'right', ...
    'FontName', 'Times New Roman', ...
    'FontSize', 11);

%% 坐标轴
xticks(ax, x);
xticklabels(ax, labels);

ylabel(ax, 'T_{air} / min', ...
    'FontName', 'Times New Roman', ...
    'Interpreter', 'tex');

title(ax, '问题一求解过程及飞机使用时间变化', ...
    'FontName', 'SimSun', ...
    'FontSize', 14);

ax.FontName = 'Times New Roman';
ax.FontSize = 11;

grid(ax, 'on');
box(ax, 'on');

ymin = lpBound - 180;
ymax = max(Tair) + 450;

ylim(ax, [ymin ymax]);
xlim(ax, [0.65 numel(x)+0.35]);


function root = projectRoot()

p = fileparts(mfilename('fullpath'));

for k = 1:8

    target = fullfile(p, '代码', 'q1', ...
        'outputs', 'q1-summary.json');

    if isfile(target)
        root = p;
        return;
    end

    parent = fileparts(p);

    if strcmp(parent, p)
        break;
    end

    p = parent;
end

error('无法自动定位 CLB_B 仓库根目录。');

end