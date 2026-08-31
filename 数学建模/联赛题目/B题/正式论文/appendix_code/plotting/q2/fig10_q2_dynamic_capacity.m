clear; clc;

root = projectRoot();
outDir = fullfile(root, 'source_code', 'q2', 'outputs');

routeFile = fullfile(outDir, 'q2-routes.csv');
assignmentFile = fullfile(outDir, 'q2-assignments.csv');
if ~isfile(routeFile) || ~isfile(assignmentFile)
    error('缺少 Q2 正式 routes/assignments CSV。');
end
R = readtable(routeFile, 'TextType', 'string');
A = readtable(assignmentFile, 'TextType', 'string');

set(groot, ...
    'defaultAxesFontName', 'Times New Roman', ...
    'defaultTextFontName', 'Times New Roman');

%% 自动选择累计服务人数/容量最大的架次（体现座位即时复用）
keys = unique(A(:, {'aircraft_type','flight_no'}), 'rows', 'stable');
ratio = zeros(height(keys),1);
counts = zeros(height(keys),1);
capacities = zeros(height(keys),1);
for i = 1:height(keys)
    kind = keys.aircraft_type(i);
    if kind == "T1"
        capacities(i) = 12;
    elseif kind == "T2"
        capacities(i) = 16;
    elseif kind == "T3"
        capacities(i) = 19;
    else
        error('检测到未知机型：%s', kind);
    end
    counts(i) = sum(A.aircraft_type == kind & A.flight_no == keys.flight_no(i));
    ratio(i) = counts(i) / capacities(i);
end
[~, idx] = max(ratio);
aircraftType = keys.aircraft_type(idx);
flightNo = keys.flight_no(idx);
capacity = capacities(idx);

%% 获取路线
route = R( ...
    R.aircraft_type == aircraftType & ...
    R.flight_no == flightNo, :);

if isempty(route)
    error('找不到选中架次的路线。');
end

route = sortrows(route, 'stop_order');

%% 获取人员
ass = A( ...
    A.aircraft_type == aircraftType & ...
    A.flight_no == flightNo, :);

stopOrder = route.stop_order;
stopNames = route.facility_id;

nStops = height(route);
nLegs = nStops - 1;

%% 按 [pickup, delivery) 计算每个航段载客量
loadByLeg = zeros(nLegs,1);

for i = 1:nLegs

    h = stopOrder(i);

    loadByLeg(i) = sum( ...
        ass.pickup_stop_order <= h & ...
        ass.delivery_stop_order > h);
end

if any(loadByLeg > capacity)
    error('检测到逐航段超容量，与正式验证结果矛盾。');
end

%% 各站上下客人数
board = zeros(nStops,1);
alight = zeros(nStops,1);

for i = 1:nStops

    h = stopOrder(i);

    board(i) = ...
        sum(ass.pickup_stop_order == h);

    alight(i) = ...
        sum(ass.delivery_stop_order == h);
end

%% 航段标签
legLabels = strings(nLegs,1);

for i = 1:nLegs
    legLabels(i) = ...
        stopNames(i) + "-" + stopNames(i+1);
end

figure('Color', 'w', ...
    'Position', [100 70 1080 720]);

tl = tiledlayout(2, 1, ...
    'TileSpacing', 'compact', ...
    'Padding', 'compact');

%% (a) 逐航段实际载客量
ax1 = nexttile;

stairs(ax1, ...
    1:nLegs, loadByLeg, '-o', ...
    'LineWidth', 1.8, ...
    'MarkerSize', 7, ...
    'MarkerFaceColor', 'w');

hold(ax1, 'on');

yline(ax1, capacity, '--', ...
    sprintf('Capacity = %d', capacity), ...
    'FontName', 'Times New Roman', ...
    'LineWidth', 1.3, ...
    'LabelHorizontalAlignment', 'left', ...
    'HandleVisibility', 'off');

xticks(ax1, 1:nLegs);
xticklabels(ax1, legLabels);

ylabel(ax1, ...
    'Passengers onboard', ...
    'FontName', 'Times New Roman');

title(ax1, ...
    '典型联合运输架次的逐航段实际载客量', ...
    'FontName', 'SimSun', ...
    'FontSize', 13);

ax1.FontName = 'Times New Roman';
ax1.FontSize = 11;

grid(ax1, 'on');
box(ax1, 'on');

for i = 1:nLegs

    text(ax1, ...
        i, loadByLeg(i) + 0.35, ...
        sprintf('%d', loadByLeg(i)), ...
        'HorizontalAlignment', 'center', ...
        'VerticalAlignment', 'bottom', ...
        'FontName', 'Times New Roman', ...
        'FontSize', 10);
end

maxLoad = max(loadByLeg);

ylim(ax1, ...
    [0, 1.28 * max([capacity maxLoad 1])]);

text(ax1, 0.025, 0.92, ...
    sprintf(['%s-%d    Total served = %d    ', ...
             'Capacity = %d    Max onboard = %d'], ...
    aircraftType, flightNo, ...
    height(ass), capacity, maxLoad), ...
    'Units', 'normalized', ...
    'FontName', 'Times New Roman', ...
    'FontSize', 10);

%% (b) 上下客变化
ax2 = nexttile;
hold(ax2, 'on');

x = 1:nStops;

hBoard = stem(ax2, ...
    x - 0.08, board, ...
    'filled', ...
    'LineWidth', 1.5, ...
    'MarkerSize', 6);

hAlight = stem(ax2, ...
    x + 0.08, -alight, ...
    'filled', ...
    'LineWidth', 1.5, ...
    'MarkerSize', 6);

yline(ax2, 0, '-', ...
    'LineWidth', 1, ...
    'HandleVisibility', 'off');

xticks(ax2, x);
xticklabels(ax2, stopNames);

ylabel(ax2, ...
    'Passenger change', ...
    'FontName', 'Times New Roman');

title(ax2, ...
    '各停靠点上下客量：同站先下后上实现座位即时复用', ...
    'FontName', 'SimSun', ...
    'FontSize', 13);

legend(ax2, ...
    [hBoard hAlight], ...
    {'Board', 'Alight'}, ...
    'Location', 'northeast', ...
    'FontName', 'Times New Roman');

ax2.FontName = 'Times New Roman';
ax2.FontSize = 11;

grid(ax2, 'on');
box(ax2, 'on');

limit = max([board; alight; 1]);

ylim(ax2, ...
    [-1.30*limit, 1.30*limit]);

text(ax2, 0.02, 0.05, ...
    '负值仅表示下客方向，实际人数均为非负值', ...
    'Units', 'normalized', ...
    'FontName', 'SimSun', ...
    'FontSize', 9);


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