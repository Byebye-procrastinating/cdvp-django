import os
import sys
path=os.path.abspath('.')
sys.path.append(path+r'\Algorithm from cpp')
import algorithm_from_cpp

import io

import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import networkx as nx

 
def visualize(G, detection_algo, format):
    mpl.use('svg')
    # 进行可视化划分，接口详解见下文

    community_set = detection_algo(G)
    # community_set = greedy_modularity_communities(G)             # 返回社区的列表，元素为每个社区的不可变集合
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
    community_center = nx.spring_layout(community_G, scale=2.5) # 对社区进行位置划分
    # community_center = nx.kamada_kawai_layout(community_G, scale=2.5)

    G_pos = {}
    for idx, community in enumerate(community_set):             # 对于每个社区内部进行建图
        communities[idx] = nx.Graph()
        for u in community:
            communities[idx].add_node(u)
            vertex_idx[u] = idx

        center = community_center[idx]                           # 获取该社区的位置
        community_pos[idx] = nx.spring_layout(communities[idx], center=center)          # 社区内部进行位置划分，围绕所在社区定的位置进行位置确定
        # community_pos[idx] = nx.random_layout(communities[idx], center=center)
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

# 根据 detection_algo 对应的算法计算 G 社区划分后, 每个社区大小的分布
# 并按照 format 的格式要求得到输出
def size_distribution(G, detection_algo, format):
    mpl.use('svg')

    community_set = detection_algo(G)
    community_size = [len(community) for community in community_set]

    fig, ax = plt.subplots(figsize=(5, 5))
    plt.stem(community_size)

    ax.set_xlabel('Community Index')
    ax.set_ylabel('Size')
    ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
    ax.yaxis.set_major_locator(ticker.MultipleLocator(1))
    plt.tight_layout()

    ret_svg = io.StringIO()
    plt.savefig(ret_svg, format='svg')
    plt.close()
    print(ret_svg)
    return ret_svg