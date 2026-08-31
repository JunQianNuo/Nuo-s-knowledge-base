clear; clc;

root = projectRoot();
outDir = fullfile(root, '代码', 'q3', 'outputs');

csvFile = fullfile(outDir, 'temporary_bottleneck.csv');
analysisFile = fullfile(outDir, 'temporary_bottleneck_summary.json');
stageBFile = fullfile(outDir, 'formal_stage_b_summary.json');

if ~isfile(csvFile)
    error('找不到 %s，请先运行 python -m q3.analyze_temporary_bottleneck', csvFile);
end

T = readtable(csvFile, 'TextType', 'string');
S = jsondecode(fileread(analysisFile));
B = jsondecode(fileread(stageBFile));

%% 必须是最新版 160/160
assert(B.temporary_served == B.temporary_total, ...
    '当前 Stage B 尚未实现 temporary 全接纳。');

if islogical(T.served)
    served = T.served;
else
    served = strcmpi(strtrim(string(T.served)), "true");
end

if ~all(served)
    error(['temporary_bottleneck.csv 仍是旧结果。', newline, ...
        '请先运行：python -m q3.analyze_temporary_bottleneck']);
end

assert(height(T) == B.temporary_total);
assert(B.temporary_certified_optimal);

%% 时间窗
earliest = datetime(T.earliest_pickup, ...
    'InputFormat', 'yyyy-MM-dd HH:mm:ss');

latest = datetime(T.latest_arrival, ...
    'InputFormat', 'yyyy-MM-dd HH:mm:ss');

windowHours = hours(latest - earliest);

%% 每人兼容机型数量
nTypes = zeros(height(T),1);

for i = 1:height(T)
    s = strtrim(T.aircraft_types(i));

    if strlength(s) > 0
        nTypes(i) = numel(split(s, ";"));
    end
end

%% 兼容飞机数
compatibleAircraft = T.compatible_aircraft_count;

%% 机型兼容人数
typeCount = [
    getValue(S.all_temporary_aircraft_type_distribution, 'T1')
    getValue(S.all_temporary_aircraft_type_distribution, 'T2')
    getValue(S.all_temporary_aircraft_type_distribution, 'T3')
    ];

%% 基地兼容人数
baseCount = [
    getValue(S.all_temporary_compatible_airport_distribution, 'A01')
    getValue(S.all_temporary_compatible_airport_distribution, 'A02')
    getValue(S.all_temporary_compatible_airport_distribution, 'A03')
    ];

%% 字体
set(groot, ...
    'defaultAxesFontName', 'Times New Roman', ...
    'defaultTextFontName', 'Times New Roman');

figure('Color', 'w', 'Position', [90 70 1180 720]);

tl = tiledlayout(2, 2, ...
    'TileSpacing', 'compact', ...
    'Padding', 'compact');

C = lines(3);

%% (a) 时间窗 vs 兼容飞机数
ax1 = nexttile;
hold(ax1, 'on');

for k = 1:3
    idx = nTypes == k;

    if ~any(idx)
        continue;
    end

    scatter(ax1, ...
        windowHours(idx), ...
        compatibleAircraft(idx), ...
        42, C(k,:), ...
        'filled', ...
        'MarkerFaceAlpha', 0.70, ...
        'DisplayName', sprintf('%d compatible type(s)', k));
end

xlabel(ax1, ...
    'Time-window width / h', ...
    'FontName', 'Times New Roman');

ylabel(ax1, ...
    'Compatible aircraft count', ...
    'FontName', 'Times New Roman');

title(ax1, ...
    '临时任务时间窗与具体飞机兼容性', ...
    'FontName', 'SimSun', ...
    'FontSize', 13);

legend(ax1, ...
    'Location', 'best', ...
    'FontName', 'Times New Roman');

grid(ax1, 'on');
box(ax1, 'on');

ax1.FontName = 'Times New Roman';
ax1.FontSize = 10.5;

%% (b) 兼容飞机数量分布
ax2 = nexttile;

edges = (min(compatibleAircraft)-0.5):1:(max(compatibleAircraft)+0.5);

histogram(ax2, ...
    compatibleAircraft, ...
    edges, ...
    'FaceAlpha', 0.8);

xlabel(ax2, ...
    'Compatible aircraft count', ...
    'FontName', 'Times New Roman');

ylabel(ax2, ...
    'Temporary persons', ...
    'FontName', 'Times New Roman');

title(ax2, ...
    '临时任务的具体飞机兼容数量分布', ...
    'FontName', 'SimSun', ...
    'FontSize', 13);

grid(ax2, 'on');
box(ax2, 'on');

ax2.FontName = 'Times New Roman';
ax2.FontSize = 10.5;

%% (c) 三机型兼容人数
ax3 = nexttile;

b = bar(ax3, 1:3, typeCount);

xticks(ax3, 1:3);
xticklabels(ax3, {'T1','T2','T3'});

ylabel(ax3, ...
    'Compatible temporary persons', ...
    'FontName', 'Times New Roman');

title(ax3, ...
    '各机型可服务的临时人员规模', ...
    'FontName', 'SimSun', ...
    'FontSize', 13);

grid(ax3, 'on');
box(ax3, 'on');

ax3.FontName = 'Times New Roman';
ax3.FontSize = 10.5;

for i = 1:3
    text(ax3, i, typeCount(i), ...
        sprintf('%d', typeCount(i)), ...
        'HorizontalAlignment', 'center', ...
        'VerticalAlignment', 'bottom', ...
        'FontName', 'Times New Roman');
end

ylim(ax3, [0 max(typeCount)*1.18]);

%% (d) Stage B 全接纳结果
ax4 = nexttile;
axis(ax4, 'off');

slack = B.B0 - B.T_air;

text(ax4, 0.50, 0.83, ...
    sprintf('%d / %d', ...
    B.temporary_served, B.temporary_total), ...
    'HorizontalAlignment', 'center', ...
    'FontName', 'Times New Roman', ...
    'FontSize', 26, ...
    'FontWeight', 'bold');

text(ax4, 0.50, 0.70, ...
    '临时任务全部接纳', ...
    'HorizontalAlignment', 'center', ...
    'FontName', 'SimSun', ...
    'FontSize', 14);

text(ax4, 0.13, 0.53, ...
    sprintf('Acceptance = %.1f%%', ...
    100*B.temporary_satisfaction_rate), ...
    'FontName', 'Times New Roman', ...
    'FontSize', 11);

text(ax4, 0.13, 0.42, ...
    sprintf('B_0 = %d min', B.B0), ...
    'FontName', 'Times New Roman', ...
    'FontSize', 11, ...
    'Interpreter', 'tex');

text(ax4, 0.13, 0.31, ...
    sprintf('Stage B T_{air} = %d min', B.T_air), ...
    'FontName', 'Times New Roman', ...
    'FontSize', 11, ...
    'Interpreter', 'tex');

text(ax4, 0.13, 0.20, ...
    sprintf('Budget slack = %d min', slack), ...
    'FontName', 'Times New Roman', ...
    'FontSize', 11);

text(ax4, 0.13, 0.09, ...
    sprintf('Status = %s, gap = %.1f%%', ...
    B.status, 100*B.temporary_gap), ...
    'FontName', 'Times New Roman', ...
    'FontSize', 11);

%% 基地兼容说明
text(ax4, 0.62, 0.53, ...
    sprintf('A01 compatible: %d', baseCount(1)), ...
    'FontName', 'Times New Roman', ...
    'FontSize', 10.5);

text(ax4, 0.62, 0.42, ...
    sprintf('A02 compatible: %d', baseCount(2)), ...
    'FontName', 'Times New Roman', ...
    'FontSize', 10.5);

text(ax4, 0.62, 0.31, ...
    sprintf('A03 compatible: %d', baseCount(3)), ...
    'FontName', 'Times New Roman', ...
    'FontSize', 10.5);


function value = getValue(S, name)

if isfield(S, name)
    value = S.(name);
else
    value = 0;
end

end


function root = projectRoot()

p = fileparts(mfilename('fullpath'));

for k = 1:8

    target = fullfile(p, ...
        '代码', 'q3', 'outputs', ...
        'q3-summary.json');

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