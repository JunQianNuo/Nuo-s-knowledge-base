clear; clc;

root = projectRoot();
outDir = fullfile(root, '代码', 'q2', 'outputs');

summaryFile = fullfile(outDir, 'q2-summary.json');
tpaxFile = fullfile(outDir, 'q2-tpax-by-category.csv');

if ~isfile(summaryFile)
    error('找不到文件：%s', summaryFile);
end

if ~isfile(tpaxFile)
    error('找不到文件：%s', tpaxFile);
end

S = jsondecode(fileread(summaryFile));

T = readtable(tpaxFile, ...
    'TextType', 'string');

set(groot, ...
    'defaultAxesFontName', 'Times New Roman', ...
    'defaultTextFontName', 'Times New Roman');

categories = ["outbound"; "return"; "shuttle"];
categoryNames = {'Outbound', 'Return', 'Shuttle'};

%% 各类联合方案 T_pax 与人数
joint = zeros(3,1);
count = zeros(3,1);

for i = 1:3
    idx = T.category == categories(i);
    joint(i) = sum(T.t_pax(idx));
    count(i) = sum(idx);
end

%% 图表规划表已核验的分类变化量
delta = [2665; 8123; -426];
baseline = joint - delta;

assert(sum(joint) == S.joint_solution.T_pax, ...
    '联合方案分类 T_pax 与 summary 不一致。');

assert(sum(baseline) == S.baseline_separated.T_pax, ...
    '分类基线 T_pax 与 summary 不一致。');

assert(sum(delta) == ...
    S.joint_solution.T_pax - S.baseline_separated.T_pax, ...
    '分类变化量与总 T_pax 变化不一致。');

%% 人均在途时间
baselineMean = baseline ./ count;
jointMean = joint ./ count;

%% 绕行比例
detourShare = 100 * sum(T.stops_between > 0) / height(T);
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