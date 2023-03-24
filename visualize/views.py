import io

from django.shortcuts import render
import networkx as nx
from networkx.algorithms.community.modularity_max \
    import greedy_modularity_communities

from .forms import GraphInputForm
from .visualization import graphviz, size_distribution


def application(request):
    graph_svg = io.StringIO()
    size_distribution_svg = io.StringIO()

    if request.method != 'POST':
        form = GraphInputForm()
    else:
        form = GraphInputForm(request.POST)
        if form.is_valid():
            graph = nx.Graph()
            edge_list = form.cleaned_data['graph_input'].split()
            ne = len(edge_list)
            for i in range(0, ne, 2):
                u, v = int(edge_list[i]), int(edge_list[i + 1])
                graph.add_edge(u, v)
            graph_svg = graphviz(graph, greedy_modularity_communities, 'svg')
            size_distribution_svg = size_distribution(
                graph, greedy_modularity_communities, 'svg')

    content = {
        'form_graph_input': form,
        'graph_svg': graph_svg.getvalue(),
        'size_distribution_svg': size_distribution_svg.getvalue(),
        }
    return render(request, 'visualize/application.html', content)


# TODO: 根据输入生成满足对应要求的图
def generate(request):
    pass

def index(request):
    return render(request, 'visualize/index.html')

def features(request):
    return render(request, 'visualize/features.html')

def about(request):
    return render(request, 'visualize/about.html')