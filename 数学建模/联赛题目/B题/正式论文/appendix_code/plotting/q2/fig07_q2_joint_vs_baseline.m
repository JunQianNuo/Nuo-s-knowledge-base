clear; clc;

root = projectRoot();
summaryFile = fullfile(root, 'source_code', 'q2', 'outputs', 'q2-summary.json');

if ~isfile(summaryFile)
    error('找不到文件：%s', summaryFile);
end

S = jsondecode(fileread(summaryFile));
B = S.baseline_separated;
J = S.joint_solution;

set(groot, 'defaultAxesFontName', 'Times New Roman', ...
           'defaultTextFontName', 'Times New Roman');

figure('Color', 'w', 'Position', [100 80 1180 650]);
tl = tiledlayout(2, 3, ...
    'TileSpacing', 'compact', ...
    'Padding', 'compact');

drawPair(nexttile, B.T_air, J.T_air, ...
    'T_{air} / min', '总飞机使用时间', false);

drawPair(nexttile, B.T_pax, J.T_pax, ...
    'T_{pax} / person-min', '人员总在途时间', false);

drawPair(nexttile, B.fuel, J.fuel, ...
    'Fuel / kg', '总燃油消耗', false);

drawPair(nexttile, B.flights, J.flights, ...
    'Flights', '总架次数', false);

drawPair(nexttile, ...
    100 * B.utilization, ...
    100 * J.utilization, ...
    'Utilization / %', '座位利用率', true);

%% 综合效果
ax = nexttile;
axis(ax, 'off');

airImprove = 100 * (B.T_air - J.T_air) / B.T_air;
fuelImprove = 100 * (B.fuel - J.fuel) / B.fuel;
flightImprove = 100 * (B.flights - J.flights) / B.flights;
paxChange = 100 * (J.T_pax - B.T_pax) / B.T_pax;
utilChange = 100 * (J.utilization - B.utilization);

text(ax, 0.04, 0.86, '联合运输综合效果', ...
    'FontName', 'SimSun', ...
    'FontSize', 14, ...
    'FontWeight', 'bold');

text(ax, 0.04, 0.65, sprintf('T_{air}:  -%.1f%%', airImprove), ...
    'FontName', 'Times New Roman', 'FontSize', 12, ...
    'Interpreter', 'tex');

text(ax, 0.04, 0.51, sprintf('Fuel:      -%.1f%%', fuelImprove), ...
    'FontName', 'Times New Roman', 'FontSize', 12);

text(ax, 0.04, 0.37, sprintf('Flights:   -%.1f%%', flightImprove), ...
    'FontName', 'Times New Roman', 'FontSize', 12);

text(ax, 0.04, 0.23, sprintf('T_{pax}:  +%.1f%%', paxChange), ...
    'FontName', 'Times New Roman', 'FontSize', 12, ...
    'Interpreter', 'tex');

text(ax, 0.04, 0.09, sprintf('Utilization: +%.1f pp', utilChange), ...
    'FontName', 'Times New Roman', 'FontSize', 12);


function drawPair(ax, b, j, yLabelText, titleText, isPercent)

plot(ax, [1 2], [b j], '-o', ...
    'LineWidth', 1.7, ...
    'MarkerSize', 7, ...
    'MarkerFaceColor', 'w');

grid(ax, 'on');
box(ax, 'on');

xlim(ax, [0.7 2.3]);
xticks(ax, [1 2]);
xticklabels(ax, {'Baseline', 'Joint'});

ax.FontName = 'Times New Roman';
ax.FontSize = 11;

ylabel(ax, yLabelText, ...
    'FontName', 'Times New Roman', ...
    'Interpreter', 'tex');

title(ax, titleText, ...
    'FontName', 'SimSun', ...
    'FontSize', 13);

if isPercent
    fmt = '%.2f';
elseif mod(b,1) == 0 && mod(j,1) == 0
    fmt = '%.0f';
else
    fmt = '%.1f';
end

text(ax, 1, b, sprintf(fmt, b), ...
    'HorizontalAlignment', 'center', ...
    'VerticalAlignment', 'bottom', ...
    'FontName', 'Times New Roman', ...
    'FontSize', 10);

text(ax, 2, j, sprintf(fmt, j), ...
    'HorizontalAlignment', 'center', ...
    'VerticalAlignment', 'bottom', ...
    'FontName', 'Times New Roman', ...
    'FontSize', 10);

v = [b j];
span = max(v) - min(v);

if span == 0
    pad = max(abs(v)) * 0.1;
else
    pad = max(span * 0.35, max(abs(v)) * 0.03);
end

if pad == 0
    pad = 1;
end

ylim(ax, [min(v)-pad, max(v)+1.5*pad]);

end


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