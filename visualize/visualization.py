import os
import sys
path=os.path.abspath('.')
sys.path.append(path+r'\Algorithm from cpp')
# import algorithm_from_cpp

import io

import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import networkx as nx

 
def graph_viz(G, detection_algo, layout_algo, is_weighted=False):
    mpl.use('svg')
    # 进行可视化划分，接口详解见下文

    # community_set: 社区的列表，元素为每个社区的集合
    if is_weighted:
        community_set = detection_algo(G, weight='weight')
    else:
        community_set = detection_algo(G)
    # community_set = algorithm_from_cpp.LabelPropagation(EDGE,len(G.nodes)) # self.algorithm
    n, nc = 0, len(community_set)                                # n - 节点数 ; nc - 社区个数
    for community in community_set:                              # 优化？
        n += len(community)

    communities = [None] * nc                                   # 每个社区的内部图
    community_pos = [None] * nc                                 # 每个社区的可视化位置
    vertex_idx = [None] * (n + 1)                               # 每个点所属社区

    community_G = nx.Graph()                                    # 缩点，对于社区进行建图
    for u in range(nc):                                         # 获取缩点的编号
        community_G.add_node(u)
    community_center = layout_algo(community_G, scale=3.5) # 对社区进行位置划分

    G_pos = {}
    for idx, community in enumerate(community_set):             # 对于每个社区内部进行建图
        communities[idx] = nx.Graph()
        for u in community:
            communities[idx].add_node(u)
            vertex_idx[u] = idx

        center = community_center[idx]                           # 获取该社区的位置
        community_pos[idx] = layout_algo(communities[idx], center=center)          # 社区内部进行位置划分，围绕所在社区定的位置进行位置确定
        G_pos.update(community_pos[idx])

    inner_edges, outer_edges = [], []                            # 社区内部边，社区外部边进行分类
    for u, v in G.edges():
        if vertex_idx[u] == vertex_idx[v]:
            inner_edges.append((u, v))
        else:
            outer_edges.append((u, v))

    fig, ax = plt.subplots(figsize=(5, 5))
    color_map = mpl.cm.get_cmap('gist_rainbow')

    for idx in range(nc):
        pos = community_pos[idx]
        if nc > 1:
            color = mpl.colors.to_hex(color_map(idx / (nc - 1)))
        else:
            color = mpl.colors.to_hex(color_map(idx))
        nx.draw_networkx_nodes(communities[idx], pos,
            node_size = 50, node_color=color, edgecolors='grey')
    nx.draw_networkx_edges(G, G_pos,
        edgelist=outer_edges, edge_color='lightgrey')               # 画社区外部边
    nx.draw_networkx_edges(G, G_pos,
        edgelist=inner_edges, edge_color='grey')                    # 画社区内部边
    # nx.draw_networkx_labels(G, G_pos, font_size=12)

    plt.axis('off')
    plt.tight_layout()

    ret_svg = io.StringIO()
    plt.savefig(ret_svg, format='svg')
    plt.close()
    return ret_svg


# 根据 detection_algo 对应的算法计算 graph 的社区划分后, 每个社区大小的分布
# 并按照 format 的格式要求得到输出
def size_distribution(graph, detection_algo, is_weighted=False):
    mpl.use('svg')

    if is_weighted:
        community_set = detection_algo(graph, weight='weight')
    else:
        community_set = detection_algo(graph)
    community_size = [len(community) for community in community_set]

    fig, ax = plt.subplots(figsize=(5, 5))
    plt.stem(community_size)

    plt.title('Size Distribution')
    ax.set_xlabel('Community Index')
    ax.set_ylabel('Size')
    ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
    ax.yaxis.set_major_locator(ticker.MultipleLocator(1))
    plt.tight_layout()

    ret_svg = io.StringIO()
    plt.savefig(ret_svg, format='svg')
    plt.close()
    return ret_svg


# 计算按 detection_algo 对应算法社区划分后, 所得社区的模块度
def calc_modularity(graph, detection_algo):
    community_set = detection_algo(graph)
    return nx.algorithms.community.quality.modularity(graph, community_set)

# 计算按 detection_algo 对应算法划分后, 所得 coverage 和 performance
def calc_partition_quality(graph, detection_algo):
    community_set = detection_algo(graph)
    return nx.algorithms.community.quality.partition_quality(
        graph, community_set)