import io

from django.shortcuts import render
import networkx as nx
from networkx.algorithms.community.modularity_max \
    import greedy_modularity_communities

from .forms import GraphInputForm, RandomGraphForm
from .visualization import graphviz, size_distribution


def index(request):
    graph_svg = io.StringIO()
    size_distribution_svg = io.StringIO()

    if request.method != 'POST':
        form = GraphInputForm()
    else:
        form = GraphInputForm(request.POST)
        if form.is_valid():
            current_data = form.cleaned_data['graph_input']

            G = nx.Graph()
            edge_list = str(current_data).split()
            ne = len(edge_list)
            for i in range(0, ne, 2):
                u, v = int(edge_list[i]), int(edge_list[i + 1])
                G.add_edge(u, v)
            graph_svg = graphviz(G, greedy_modularity_communities, 'svg')
            size_distribution_svg = size_distribution(
                G, greedy_modularity_communities, 'svg')

    content = {
        'form_graph_input': form,
        'form_random_graph': RandomGraphForm(),
        'graph_svg': graph_svg.getvalue(),
        'size_distribution_svg': size_distribution_svg.getvalue(),
        }
    return render(request, 'visualize/index.html', content)


# 根据输入的点数和边数生成随机图
def generate_random_graph(request):
    form_graph_input = GraphInputForm()

    if request.method != 'POST':
        form = RandomGraphForm()
    else:
        form = RandomGraphForm(request.POST)
        if form.is_valid():
            node_count = form.cleaned_data['node_count']
            edge_count = form.cleaned_data['edge_count']

    content = {
        'form_graph_input': form_graph_input,
        'form_random_graph': form,
        'graph_svg': '',
        'size_distribution_svg': '',
        }
    return render(request, 'visualize/index.html', content)

def features(request):
    return render(request, 'visualize/features.html')

def about(request):
    return render(request, 'visualize/about.html')