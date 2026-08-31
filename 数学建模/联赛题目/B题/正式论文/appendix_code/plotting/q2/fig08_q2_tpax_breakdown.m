clear; clc;

root = projectRoot();
outDir = fullfile(root, 'source_code', 'q2', 'outputs');

summaryFile = fullfile(outDir, 'q2-summary.json');
aggregateFile = fullfile(outDir, 'q2-tpax-aggregate.csv');
detourFile = fullfile(outDir, 'q2-detour-summary.csv');
if ~isfile(summaryFile) || ~isfile(aggregateFile) || ~isfile(detourFile)
    error('缺少 Q2 图8所需的正式汇总数据。');
end
S = jsondecode(fileread(summaryFile));
T = readtable(aggregateFile, 'TextType', 'string');
D = readtable(detourFile);

set(groot, ...
    'defaultAxesFontName', 'Times New Roman', ...
    'defaultTextFontName', 'Times New Roman');

categoryNames = {'Outbound', 'Return', 'Shuttle'};
joint = T.joint_T_pax;
baseline = T.baseline_T_pax;
delta = T.delta;
count = T.count;
assert(sum(joint) == S.joint_solution.T_pax);
assert(sum(baseline) == S.baseline_separated.T_pax);
baselineMean = baseline ./ count;
jointMean = joint ./ count;
detourShare = 100 * D.detour_share(1);
directShare = 100 - detourShare;

figure('Color', 'w', 'Position', [80 120 1220 430]);

tl = tiledlayout(1, 3, ...
    'TileSpacing', 'compact', ...
    'Padding', 'compact');

%% (a) 各类需求人均 T_pax
ax1 = nexttile;

Y = [baselineMean, jointMean];

b = bar(ax1, Y, 'grouped');

xticks(ax1, 1:3);
xticklabels(ax1, categoryNames);

ylabel(ax1, 'Mean T_{pax} / min', ...
    'FontName', 'Times New Roman', ...
    'Interpreter', 'tex');

title(ax1, '三类需求人均在途时间对比', ...
    'FontName', 'SimSun', ...
    'FontSize', 13);

legend(ax1, {'Baseline', 'Joint'}, ...
    'FontName', 'Times New Roman', ...
    'Location', 'northwest');

ax1.FontName = 'Times New Roman';
ax1.FontSize = 11;

grid(ax1, 'on');
box(ax1, 'on');

for k = 1:2
    x = b(k).XEndPoints;
    y = b(k).YEndPoints;

    for i = 1:numel(x)
        text(ax1, x(i), y(i), ...
            sprintf('%.2f', y(i)), ...
            'HorizontalAlignment', 'center', ...
            'VerticalAlignment', 'bottom', ...
            'FontName', 'Times New Roman', ...
            'FontSize', 9);
    end
end

ylim(ax1, [0, max(Y, [], 'all') * 1.18]);

%% (b) 三类需求总 T_pax 变化
ax2 = nexttile;
hold(ax2, 'on');

stem(ax2, 1:3, delta, ...
    'filled', ...
    'LineWidth', 1.6, ...
    'MarkerSize', 7);

yline(ax2, 0, '--', ...
    'LineWidth', 1.1, ...
    'HandleVisibility', 'off');

xticks(ax2, 1:3);
xticklabels(ax2, categoryNames);

ylabel(ax2, '\DeltaT_{pax} / person-min', ...
    'FontName', 'Times New Roman', ...
    'Interpreter', 'tex');

title(ax2, '各类需求的在途时间增减', ...
    'FontName', 'SimSun', ...
    'FontSize', 13);

ax2.FontName = 'Times New Roman';
ax2.FontSize = 11;

grid(ax2, 'on');
box(ax2, 'on');

for i = 1:3

    pct = 100 * delta(i) / baseline(i);

    if delta(i) >= 0
        va = 'bottom';
    else
        va = 'top';
    end

    text(ax2, i, delta(i), ...
        sprintf('%+d  (%+.1f%%)', delta(i), pct), ...
        'HorizontalAlignment', 'center', ...
        'VerticalAlignment', va, ...
        'FontName', 'Times New Roman', ...
        'FontSize', 9);
end

%% (c) 绕行比例
ax3 = nexttile;

labels = { ...
    sprintf('Direct %.1f%%', directShare), ...
    sprintf('Detour %.1f%%', detourShare)};

p = pie(ax3, ...
    [directShare detourShare], ...
    labels);

txt = findobj(p, 'Type', 'text');

set(txt, ...
    'FontName', 'Times New Roman', ...
    'FontSize', 10);

title(ax3, '人员运输中的额外经停占比', ...
    'FontName', 'SimSun', ...
    'FontSize', 13);


function root = projectRoot()

p = fileparts(mfilename('fullpath'));

for k = 1:8

    target = fullfile(p, 'source_code', 'q2', ...
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

error('无法自动定位支撑材料根目录。');

end