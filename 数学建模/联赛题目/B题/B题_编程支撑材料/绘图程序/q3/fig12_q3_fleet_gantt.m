clear; clc;

root = projectRoot();

routeFile = fullfile(root, ...
    '代码', 'q3', 'outputs', ...
    'q3-routes.csv');

if ~isfile(routeFile)
    error('找不到文件：%s', routeFile);
end

R = readtable(routeFile, ...
    'TextType', 'string');

%% 时间
R.arrival_time = parseDateTime(R.arrival_time);
R.departure_time = parseDateTime(R.departure_time);

%% 题面24架具体飞机
bases = ["A01","A02","A03"];
types = ["T1","T2","T3"];

counts = [
    3 3 2
    2 4 2
    2 3 3
    ];

allIDs = strings(0,1);

for b = 1:3
    for t = 1:3
        for h = 1:counts(b,t)

            allIDs(end+1,1) = sprintf( ...
                '%s-%s-H%02d', ...
                bases(b), types(t), h);

        end
    end
end

assert(numel(allIDs) == 24);

%% 提取架次
key = R.aircraft_id + "#" + string(R.flight_no);

[uKey, ~, groupID] = unique(key, 'stable');
nFlights = numel(uKey);

flightAircraft = strings(nFlights,1);
flightType = strings(nFlights,1);

startTime = NaT(nFlights,1);
endTime = NaT(nFlights,1);

for i = 1:nFlights

    idx = find(groupID == i);

    flight = sortrows(R(idx,:), 'stop_order');

    flightAircraft(i) = flight.aircraft_id(1);

    idPart = split(flightAircraft(i), "-");
    flightType(i) = idPart(2);

    startTime(i) = flight.departure_time(1);
    endTime(i) = flight.arrival_time(end);

end

assert(all(~isnat(startTime)));
assert(all(~isnat(endTime)));

%% 规则复核
assert(all(timeofday(startTime) >= hours(6)));
assert(all(timeofday(startTime) <= hours(18)));
assert(all(timeofday(endTime) <= hours(20)));

assert(all( ...
    dateshift(startTime,'start','day') == ...
    dateshift(endTime,'start','day')));

[found, yPos] = ismember( ...
    flightAircraft, allIDs);

assert(all(found));

%% 最小实际周转
minTurnaround = inf;

for i = 1:numel(allIDs)

    idx = find(flightAircraft == allIDs(i));

    if numel(idx) < 2
        continue;
    end

    [s, order] = sort(startTime(idx));
    e = endTime(idx(order));

    gap = minutes( ...
        s(2:end) - e(1:end-1));

    minTurnaround = ...
        min(minTurnaround, min(gap));

end

assert(minTurnaround >= 30);

%% 横轴
horizon = datetime(2026,8,3,0,0,0);

xStart = hours(startTime - horizon);
xEnd = hours(endTime - horizon);

%% 绘图
set(groot, ...
    'defaultAxesFontName', 'Times New Roman', ...
    'defaultTextFontName', 'Times New Roman');

figure('Color', 'w', ...
    'Position', [50 60 1450 770]);

tl = tiledlayout(1,4, ...
    'TileSpacing','compact', ...
    'Padding','compact');

%% 甘特主图
ax1 = nexttile(tl,1,[1 3]);
hold(ax1,'on');

yMin = 0.5;
yMax = 24.5;

%% 每日运营区间
for d = 0:6

    x0 = 24*d;

    % 00:00-06:00
    patch(ax1, ...
        [x0 x0+6 x0+6 x0], ...
        [yMin yMin yMax yMax], ...
        [0.94 0.94 0.94], ...
        'EdgeColor','none', ...
        'HandleVisibility','off');

    % 20:00-24:00
    patch(ax1, ...
        [x0+20 x0+24 x0+24 x0+20], ...
        [yMin yMin yMax yMax], ...
        [0.94 0.94 0.94], ...
        'EdgeColor','none', ...
        'HandleVisibility','off');

    % 最晚起飞18:00
    xline(ax1, x0+18, ':', ...
        'LineWidth',0.8, ...
        'HandleVisibility','off');

    if d > 0
        xline(ax1, x0, '-', ...
            'LineWidth',0.7, ...
            'HandleVisibility','off');
    end
end

%% 架次
C = lines(3);

for i = 1:nFlights

    if flightType(i) == "T1"
        c = C(1,:);
    elseif flightType(i) == "T2"
        c = C(2,:);
    else
        c = C(3,:);
    end

    % 正式架次
    plot(ax1, ...
        [xStart(i) xEnd(i)], ...
        [yPos(i) yPos(i)], ...
        '-', ...
        'Color', c, ...
        'LineWidth', 5, ...
        'HandleVisibility','off');

    % 返场后30min周转
    plot(ax1, ...
        [xEnd(i) xEnd(i)+0.5], ...
        [yPos(i) yPos(i)], ...
        '-', ...
        'Color', [0.68 0.68 0.68], ...
        'LineWidth', 2, ...
        'HandleVisibility','off');
end

%% 图例
h1 = plot(ax1,nan,nan,'-', ...
    'Color',C(1,:), ...
    'LineWidth',5);

h2 = plot(ax1,nan,nan,'-', ...
    'Color',C(2,:), ...
    'LineWidth',5);

h3 = plot(ax1,nan,nan,'-', ...
    'Color',C(3,:), ...
    'LineWidth',5);

h4 = plot(ax1,nan,nan,'-', ...
    'Color',[0.68 0.68 0.68], ...
    'LineWidth',2);

legend(ax1, ...
    [h1 h2 h3 h4], ...
    {'T1','T2','T3','30 min turnaround'}, ...
    'Location','southoutside', ...
    'Orientation','horizontal', ...
    'FontName','Times New Roman');

%% 坐标
yticks(ax1,1:24);
yticklabels(ax1,allIDs);

ax1.YDir = 'reverse';
ax1.FontName = 'Times New Roman';
ax1.FontSize = 8.5;

xlim(ax1,[0 168]);
ylim(ax1,[0.5 24.5]);

dayCenters = 12 + 24*(0:6);

xticks(ax1,dayCenters);
xticklabels(ax1, ...
    {'08-03','08-04','08-05','08-06', ...
     '08-07','08-08','08-09'});

xlabel(ax1,'Date', ...
    'FontName','Times New Roman');

ylabel(ax1,'Aircraft ID', ...
    'FontName','Times New Roman');

title(ax1, ...
    '24 架具体飞机的 7 天实际排班', ...
    'FontName','SimSun', ...
    'FontSize',13);

grid(ax1,'on');
box(ax1,'on');

activeAircraft = ...
    numel(unique(flightAircraft));

text(ax1,0.01,0.985, ...
    sprintf(['Flights = %d    ', ...
    'Active aircraft = %d / 24    ', ...
    'Minimum turnaround = %.0f min'], ...
    nFlights, ...
    activeAircraft, ...
    minTurnaround), ...
    'Units','normalized', ...
    'VerticalAlignment','top', ...
    'FontName','Times New Roman', ...
    'FontSize',9.5);

%% 右侧机型任务规模
ax2 = nexttile(tl,4);
hold(ax2,'on');

flightCount = zeros(3,1);
airHours = zeros(3,1);
activeCount = zeros(3,1);

for t = 1:3

    idx = flightType == types(t);

    flightCount(t) = sum(idx);

    airHours(t) = sum( ...
        hours(endTime(idx)-startTime(idx)));

    activeCount(t) = ...
        numel(unique(flightAircraft(idx)));

end

for t = 1:3

    scatter(ax2, ...
        flightCount(t), ...
        airHours(t), ...
        95*activeCount(t), ...
        C(t,:), ...
        'filled');

    text(ax2, ...
        flightCount(t), ...
        airHours(t), ...
        ['  ',char(types(t))], ...
        'FontName','Times New Roman', ...
        'FontSize',11, ...
        'FontWeight','bold');
end

xlabel(ax2,'Flights', ...
    'FontName','Times New Roman');

ylabel(ax2,'Aircraft time / h', ...
    'FontName','Times New Roman');

title(ax2, ...
    '各机型任务规模', ...
    'FontName','SimSun', ...
    'FontSize',13);

grid(ax2,'on');
box(ax2,'on');

ax2.FontName = 'Times New Roman';
ax2.FontSize = 10;

text(ax2,0.04,0.05, ...
    'Bubble size = active aircraft', ...
    'Units','normalized', ...
    'FontName','Times New Roman', ...
    'FontSize',9);


function dt = parseDateTime(x)

x = string(x);

dt = NaT(size(x));

valid = ...
    ~ismissing(x) & ...
    strlength(strtrim(x)) > 0;

dt(valid) = datetime( ...
    x(valid), ...
    'InputFormat','yyyy-MM-dd HH:mm');

end


function root = projectRoot()

p = fileparts(mfilename('fullpath'));

for k = 1:8

    target = fullfile(p, ...
        '代码','q3','outputs', ...
        'q3-summary.json');

    if isfile(target)
        root = p;
        return;
    end

    parent = fileparts(p);

    if strcmp(parent,p)
        break;
    end

    p = parent;
end

error('无法自动定位 CLB_B 仓库根目录。');

end