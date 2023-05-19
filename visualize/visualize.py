import io

import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import networkx as nx

# 进行划分可视化
# community_set: 社区的列表，元素为每个社区的集合
def graph_viz(graph, community_set, layout_algo):
    mpl.use('svg')

    # n: 结点个数
    n = sum([len(comunity) for comunity in community_set])
    # nc: 社区个数
    nc = len(community_set)

    # 每个社区的内部图
    communities = [None] * nc
    # 每个社区的可视化位置
    community_pos = [None] * nc
    # 每个点所属社区
    vertex_idx = [None] * (n + 1)

    community_graph = nx.Graph()
    for u in range(nc):
        community_graph.add_node(u)
    # 对社区进行位置划分
    community_center = layout_algo(community_graph, scale=3.5)

    graph_pos = {}
    # 对于每个社区内部进行建图
    for idx, community in enumerate(community_set):
        communities[idx] = nx.Graph()
        for u in community:
            communities[idx].add_node(u)
            vertex_idx[u] = idx

        # 获取该社区的位置
        center = community_center[idx]
        # 社区内部进行位置划分，围绕所在社区定的位置进行位置确定
        community_pos[idx] = layout_algo(communities[idx], center=center)
        graph_pos.update(community_pos[idx])

    # 社区内部边，社区外部边进行分类
    inner_edges, outer_edges = [], []
    for u, v in graph.edges():
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
    # 画社区外部边
    nx.draw_networkx_edges(graph, graph_pos,
        edgelist=outer_edges, edge_color='lightgrey')
    # 画社区内部边
    nx.draw_networkx_edges(graph, graph_pos,
        edgelist=inner_edges, edge_color='grey')                    
    # nx.draw_networkx_labels(graph, graph_pos, font_size=12)

    plt.axis('off')
    plt.tight_layout()

    ret_svg = io.StringIO()
    plt.savefig(ret_svg, format='svg')
    plt.close()
    return ret_svg


# 根据 community_set 得到社区的大小分布
def size_distribution(community_set):
    mpl.use('svg')

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