from django.shortcuts import render
import networkx as nx
from networkx.algorithms.community.modularity_max \
    import greedy_modularity_communities

from .forms import GraphInputForm
from .visualization import visualize, size_distribution


def index(request):
    graph_svg_str, size_distribution_svg_str = '', ''

    if request.method != 'POST':
        form = GraphInputForm()
    else:
        form = GraphInputForm(request.POST)
        if form.is_valid():
            GraphInput = form.save(commit=False)

            G = nx.Graph()
            edge_list = str(GraphInput.graph_data).split()
            ne = len(edge_list)
            for i in range(0, ne, 2):
                u, v = int(edge_list[i]), int(edge_list[i + 1])
                G.add_edge(u, v)
            graph_svg = visualize(G, greedy_modularity_communities, 'svg')
            graph_svg_str = graph_svg.getvalue()
            size_distribution_svg = size_distribution(
                G, greedy_modularity_communities, 'svg')
            size_distribution_svg_str = size_distribution_svg.getvalue()

    content = {
        'form': form,
        'graph_svg': graph_svg_str,
        'size_distribution_svg': size_distribution_svg_str,
        }
    return render(request, 'visualize/index.html', content)

def features(request):
    return render(request, 'visualize/features.html')

def about(request):
    return render(request, 'visualize/about.html')