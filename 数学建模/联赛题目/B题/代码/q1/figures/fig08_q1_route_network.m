clear; clc; close all

fontCN = 'SimSun';
fontEN = 'Times New Roman';

p = fileparts(mfilename('fullpath'));
if isfolder(fullfile(p,'outputs'))
    outDir = fullfile(p,'outputs');
else
    outDir = fullfile(fileparts(p),'outputs');
end

T = readtable(fullfile(outDir,'q1-routes.csv'), ...
    'TextType','string','VariableNamingRule','preserve');

[Gid,~,~] = findgroups(T.aircraft_type,T.flight_no);

src = strings(0,1);
dst = strings(0,1);

for g = 1:max(Gid)
    S = T(Gid==g,:);
    S = sortrows(S,'stop_order');

    nodes = S.facility_id;

    src = [src; nodes(1:end-1)]; %#ok<AGROW>
    dst = [dst; nodes(2:end)];   %#ok<AGROW>
end

key = src + "->" + dst;

[uKey,~,idx] = unique(key);
freq = accumarray(idx,1);

[~,order] = sort(freq,'descend');
K = min(30,numel(order));
order = order(1:K);

topKey = uKey(order);
topFreq = freq(order);

parts = split(topKey,"->");
s = parts(:,1);
t = parts(:,2);

G = digraph(s,t,topFreq);

figure('Color','w','Position',[150 80 900 650]);

P = plot(G, ...
    'Layout','force', ...
    'ArrowSize',8, ...
    'MarkerSize',5, ...
    'LineWidth',1);

P.EdgeCData = G.Edges.Weight;
colormap(parula)

cb = colorbar;
cb.FontName = fontEN;
cb.Label.String = '航段使用次数';
cb.Label.FontName = fontCN;

% 航段频率越高，线越粗
w = G.Edges.Weight;

for i = 1:numedges(G)
    e = G.Edges.EndNodes(i,:);
    lw = 0.6 + 3*w(i)/max(w);

    highlight(P,e(1),e(2),'LineWidth',lw);
end

% 只标机场和网络中连接度最高的部分设施
deg = indegree(G) + outdegree(G);
[~,rank] = sort(deg,'descend');

labels = strings(numnodes(G),1);
airport = startsWith(string(G.Nodes.Name),"A");

labels(airport) = string(G.Nodes.Name(airport));

nShow = min(12,numnodes(G));
labels(rank(1:nShow)) = string(G.Nodes.Name(rank(1:nShow)));

P.NodeLabel = labels;
P.NodeFontName = fontEN;
P.NodeFontSize = 9;

airportNames = string(G.Nodes.Name(airport));

highlight(P,airportNames, ...
    'NodeColor',[0.85 0.25 0.20], ...
    'Marker','s', ...
    'MarkerSize',9);

title('高频航段网络拓扑（前30条航段）','FontName',fontCN)

axis off