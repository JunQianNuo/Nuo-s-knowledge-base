clear; clc;

root = projectRoot();
outDir = fullfile(root, 'source_code', 'q1', 'outputs');

routeFile = fullfile(outDir, 'q1-routes.csv');
assignmentFile = fullfile(outDir, 'q1-assignments.csv');

if ~isfile(routeFile) || ~isfile(assignmentFile)
    error('缺少 Q1 正式 routes/assignments CSV。');
end

R = readtable(routeFile, 'TextType', 'string');
A = readtable(assignmentFile, 'TextType', 'string');

set(groot, ...
    'defaultAxesFontName', 'Times New Roman', ...
    'defaultTextFontName', 'Times New Roman');

%% 自动选择含加油且海上停靠次数最多的真实架次
keys = unique(R(:, {'aircraft_type','flight_no'}), 'rows', 'stable');
score = -ones(height(keys),1);
for i = 1:height(keys)
    rr = R(R.aircraft_type == keys.aircraft_type(i) & R.flight_no == keys.flight_no(i), :);
    if any(rr.refuel == 1)
        score(i) = sum(startsWith(rr.facility_id, "F"));
    end
end
if all(score < 0)
    error('正式方案中未找到含加油的架次。');
end
[~, idx] = max(score);
aircraftType = keys.aircraft_type(idx);
flightNo = keys.flight_no(idx);
ass = A(A.aircraft_type == aircraftType & A.flight_no == flightNo, :);
passengers = height(ass);

%% 机型容量
switch aircraftType
    case "T1"
        capacity = 12;
    case "T2"
        capacity = 16;
    case "T3"
        capacity = 19;
    otherwise
        error('未知机型：%s', aircraftType);
end

%% 获取路线
route = R( ...
    R.aircraft_type == aircraftType & ...
    R.flight_no == flightNo, :);

route = sortrows(route, 'stop_order');

nodes = route.facility_id;
refuel = route.refuel;

nNodes = height(route);
nLegs = nNodes - 1;

%% 距离矩阵
distanceFile = findDistanceFile(root);

D = readtable(distanceFile, ...
    'TextType', 'string', ...
    'VariableNamingRule', 'preserve');

legDistance = zeros(nLegs,1);

for i = 1:nLegs

    from = nodes(i);
    to = nodes(i+1);

    row = find(D.from_id == from, 1);

    if isempty(row)
        error('距离矩阵中找不到节点：%s', from);
    end

    legDistance(i) = D{row, char(to)};
end

%% 由最终 assignments 直接恢复各停靠点下机人数
unload = zeros(nNodes,1);
for i = 1:nNodes
    h = route.stop_order(i);
    unload(i) = sum(ass.delivery_stop_order == h);
end
if sum(unload) ~= passengers
    error('人员下机人数与 assignments 不一致。');
end

%% 逐航段机上人数
loadByLeg = zeros(nLegs,1);

remaining = passengers;

for i = 1:nLegs

    loadByLeg(i) = remaining;

    nextNode = i + 1;
    remaining = remaining - unload(nextNode);
end

if any(loadByLeg > capacity)
    error('检测到超容量，与正式验证结果矛盾。');
end

%% 单架次距离加权座位利用率
PK = sum(loadByLeg .* legDistance);
AK = capacity * sum(legDistance);

flightUtilization = PK / AK;

%% 绘图
figure('Color', 'w', ...
    'Position', [100 80 1100 690]);

tl = tiledlayout(2, 1, ...
    'TileSpacing', 'compact', ...
    'Padding', 'compact');

%% (a) 真实物理路线
ax1 = nexttile;
hold(ax1, 'on');

x = 1:nNodes;

routeColor = [0 0.4470 0.7410];
airportColor = [0 0.4470 0.7410];
facilityColor = [0.8500 0.3250 0.0980];
refuelColor = [0.4660 0.6740 0.1880];

%% 航段箭头
for i = 1:nLegs

    quiver(ax1, ...
        x(i), 0, ...
        0.82, 0, ...
        0, ...
        'Color', routeColor, ...
        'LineWidth', 1.6, ...
        'MaxHeadSize', 0.28, ...
        'HandleVisibility', 'off');

    text(ax1, ...
        i + 0.48, -0.18, ...
        sprintf('%.0f km', legDistance(i)), ...
        'HorizontalAlignment', 'center', ...
        'FontName', 'Times New Roman', ...
        'FontSize', 9);
end

%% 节点
for i = 1:nNodes

    isAirport = startsWith(nodes(i), "A");

    if isAirport

        scatter(ax1, x(i), 0, ...
            95, ...
            airportColor, ...
            's', ...
            'filled', ...
            'HandleVisibility', 'off');

    elseif refuel(i) == 1

        scatter(ax1, x(i), 0, ...
            105, ...
            refuelColor, ...
            'd', ...
            'filled', ...
            'HandleVisibility', 'off');

    else

        scatter(ax1, x(i), 0, ...
            85, ...
            facilityColor, ...
            'o', ...
            'filled', ...
            'HandleVisibility', 'off');
    end

    text(ax1, ...
        x(i), 0.15, ...
        nodes(i), ...
        'HorizontalAlignment', 'center', ...
        'FontName', 'Times New Roman', ...
        'FontSize', 10);
end

%% 图例
hAirport = scatter(ax1, nan, nan, ...
    80, airportColor, 's', 'filled');

hFacility = scatter(ax1, nan, nan, ...
    80, facilityColor, 'o', 'filled');

hRefuel = scatter(ax1, nan, nan, ...
    85, refuelColor, 'd', 'filled');

legend(ax1, ...
    [hAirport hFacility hRefuel], ...
    {'机场', '海上设施', '本架次加油停靠'}, ...
    'FontName', 'SimSun', ...
    'FontSize', 9, ...
    'Location', 'northeast', ...
    'Box', 'off');

axis(ax1, 'off');

xlim(ax1, [0.65 nNodes+0.35]);
ylim(ax1, [-0.42 0.38]);

title(ax1, ...
    sprintf('典型实际架次路线（%s-%d）', ...
    aircraftType, flightNo), ...
    'FontName', 'SimSun', ...
    'FontSize', 13);

%% 基本信息
text(ax1, 0.02, 0.89, ...
    sprintf(['Passengers = %d    Capacity = %d    ', ...
             'Offshore stops = %d'], ...
    passengers, capacity, sum(startsWith(nodes, "F"))), ...
    'Units', 'normalized', ...
    'FontName', 'Times New Roman', ...
    'FontSize', 10);

%% (b) 逐航段载客量
ax2 = nexttile;
hold(ax2, 'on');

stairs(ax2, ...
    1:nLegs, loadByLeg, '-o', ...
    'LineWidth', 1.8, ...
    'MarkerSize', 7, ...
    'MarkerFaceColor', 'w');

yline(ax2, capacity, '--', ...
    sprintf('Capacity = %d', capacity), ...
    'LineWidth', 1.3, ...
    'FontName', 'Times New Roman', ...
    'LabelHorizontalAlignment', 'right', ...
    'HandleVisibility', 'off');

legLabels = strings(nLegs,1);

for i = 1:nLegs
    legLabels(i) = nodes(i) + "-" + nodes(i+1);
end

xticks(ax2, 1:nLegs);
xticklabels(ax2, legLabels);

ylabel(ax2, ...
    'Passengers onboard', ...
    'FontName', 'Times New Roman');

title(ax2, ...
    '逐航段载客量与距离加权座位利用率', ...
    'FontName', 'SimSun', ...
    'FontSize', 13);

ax2.FontName = 'Times New Roman';
ax2.FontSize = 11;

grid(ax2, 'on');
box(ax2, 'on');

for i = 1:nLegs

    if loadByLeg(i) == capacity
        offset = -0.65;
        va = 'top';
    else
        offset = 0.35;
        va = 'bottom';
    end

    text(ax2, ...
        i, loadByLeg(i) + offset, ...
        sprintf('%d', loadByLeg(i)), ...
        'HorizontalAlignment', 'center', ...
        'VerticalAlignment', va, ...
        'FontName', 'Times New Roman', ...
        'FontSize', 10);
end

ylim(ax2, [0 capacity * 1.28]);

text(ax2, 0.98, 0.91, ...
    sprintf('Flight utilization = %.2f%%', ...
    100 * flightUtilization), ...
    'Units', 'normalized', ...
    'HorizontalAlignment', 'right', ...
    'FontName', 'Times New Roman', ...
    'FontSize', 10);


function root = projectRoot()

p = fileparts(mfilename('fullpath'));

for k = 1:8

    if isfile(fullfile(p, 'source_code', 'q1', ...
            'outputs', 'q1-summary.json'))

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


function file = findDistanceFile(root)

files = dir(fullfile(root, '**', 'distances.csv'));

if isempty(files)
    error('项目中找不到 distances.csv。');
end

if numel(files) == 1

    file = fullfile(files(1).folder, files(1).name);
    return;
end

for i = 1:numel(files)

    if contains(files(i).folder, 'B题-附件')

        file = fullfile(files(i).folder, files(i).name);
        return;
    end
end

file = fullfile(files(1).folder, files(1).name);

end
