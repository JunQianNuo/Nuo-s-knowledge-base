clear; clc;

root = projectRoot();

historyFile = fullfile(root, '代码', 'q2', ...
    'outputs', 'q2-history.csv');

if ~isfile(historyFile)
    error('找不到文件：%s', historyFile);
end

H = readtable(historyFile, ...
    'TextType', 'string');

set(groot, ...
    'defaultAxesFontName', 'Times New Roman', ...
    'defaultTextFontName', 'Times New Roman');

stageNames = { ...
    'T_{air}', ...
    'T_{pax}', ...
    'Fuel', ...
    'Flights', ...
    'Utilization'};

obj = H.objective;
bound = H.best_bound;

%% 前四阶段 incumbent-bound 相对差距
gap = nan(height(H),1);

for i = 1:min(4,height(H))

    if ~isnan(obj(i)) && obj(i) ~= 0
        gap(i) = ...
            100 * abs(obj(i) - bound(i)) / abs(obj(i));
    end

end

figure('Color', 'w', 'Position', [180 70 920 720]);

tl = tiledlayout(2, 1, ...
    'TileSpacing', 'compact', ...
    'Padding', 'compact');

%% (a) 前四阶段求解差距
ax1 = nexttile;
hold(ax1, 'on');

for i = 1:4

    plot(ax1, ...
        [0 gap(i)], [i i], '-', ...
        'LineWidth', 1.6);

    scatter(ax1, ...
        gap(i), i, 60, ...
        'filled');

    text(ax1, ...
        gap(i), i, ...
        sprintf('  %.1f%%', gap(i)), ...
        'VerticalAlignment', 'middle', ...
        'FontName', 'Times New Roman', ...
        'FontSize', 10);
end

yticks(ax1, 1:4);
yticklabels(ax1, stageNames(1:4));

ylim(ax1, [0.5 4.5]);

xlabel(ax1, ...
    'Relative incumbent-bound difference / %', ...
    'FontName', 'Times New Roman');

title(ax1, ...
    '前四级子问题的求解器相对差距', ...
    'FontName', 'SimSun', ...
    'FontSize', 13);

ax1.FontName = 'Times New Roman';
ax1.FontSize = 11;
ax1.YDir = 'reverse';

grid(ax1, 'on');
box(ax1, 'on');

gapMax = max(gap(1:4), [], 'omitnan');

if gapMax <= 0
    gapMax = 1;
end

xlim(ax1, [0, 1.18 * gapMax]);

text(ax1, 0.98, 0.94, ...
    'Stage 2-4 conditioned on uncertified parent', ...
    'Units', 'normalized', ...
    'HorizontalAlignment', 'right', ...
    'FontName', 'Times New Roman', ...
    'FontSize', 9);

%% (b) 求解时间
ax2 = nexttile;

plot(ax2, ...
    1:height(H), H.seconds, '-o', ...
    'LineWidth', 1.7, ...
    'MarkerSize', 7, ...
    'MarkerFaceColor', 'w');

xticks(ax2, 1:height(H));
xticklabels(ax2, stageNames);

ylabel(ax2, ...
    'Solver time / s', ...
    'FontName', 'Times New Roman');

title(ax2, ...
    '五级词典序各阶段实际求解时间', ...
    'FontName', 'SimSun', ...
    'FontSize', 13);

ax2.FontName = 'Times New Roman';
ax2.FontSize = 11;

grid(ax2, 'on');
box(ax2, 'on');

for i = 1:height(H)

    text(ax2, i, H.seconds(i), ...
        sprintf('%.0f', H.seconds(i)), ...
        'HorizontalAlignment', 'center', ...
        'VerticalAlignment', 'bottom', ...
        'FontName', 'Times New Roman', ...
        'FontSize', 10);
end

ylim(ax2, ...
    [0, max(H.seconds) * 1.18]);

text(ax2, 0.02, 0.91, ...
    'All 5 stages: FEASIBLE', ...
    'Units', 'normalized', ...
    'FontName', 'Times New Roman', ...
    'FontSize', 10);


function root = projectRoot()

p = fileparts(mfilename('fullpath'));

for k = 1:8

    target = fullfile(p, '代码', 'q2', ...
        'outputs', 'q2-summary.json');

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