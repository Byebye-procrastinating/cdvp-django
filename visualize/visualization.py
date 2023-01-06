import io

import matplotlib as mpl
import matplotlib.pyplot as plt
import networkx as nx
from networkx.algorithms.community.modularity_max \
    import greedy_modularity_communities

 
def visualize(G, format):
    mpl.use('svg')

    community_set = greedy_modularity_communities(G)
    n, nc = 0, len(community_set)
    for community in community_set:
        n += len(community)

    communities = [None] * nc
    community_pos = [None] * nc
    vertex_idx = [None] * (n + 1)

    community_G = nx.Graph()
    for u in range(nc):
        community_G.add_node(u)
    community_center = nx.spring_layout(community_G, scale=2.5)
    # community_center = nx.kamada_kawai_layout(community_G, scale=2.5)

    G_pos = {}
    for idx, community in enumerate(community_set):
        communities[idx] = nx.Graph()
        for u in community:
            communities[idx].add_node(u)
            vertex_idx[u] = idx

        center = community_center[idx]
        community_pos[idx] = nx.spring_layout(communities[idx], center=center)
        # community_pos[idx] = nx.random_layout(communities[idx], center=center)
        G_pos.update(community_pos[idx])

    inner_edges, outer_edges = [], []
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
        edgelist=outer_edges, edge_color='lightgrey')
    nx.draw_networkx_edges(G, G_pos,
        edgelist=inner_edges, edge_color='grey')
    # nx.draw_networkx_labels(G, G_pos, font_size=12)

    plt.axis('off')
    plt.tight_layout()

    ret_svg = io.StringIO()
    plt.savefig(ret_svg, format='svg')
    plt.close()
    return ret_svg