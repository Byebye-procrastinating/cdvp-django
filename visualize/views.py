import io

from django.shortcuts import render
from django.http import FileResponse
import networkx as nx

from .forms import GraphInputForm
from .visualization import visualize


def index(request):
    graph_svg_str = ''

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
            graph_svg = visualize(G, 'svg')
            graph_svg_str = graph_svg.getvalue()

    content = {'form': form, 'graph_svg': graph_svg_str }
    return render(request, 'visualize/index.html', content)

def features(request):
    return render(request, 'visualize/features.html')

def about(request):
    return render(request, 'visualize/about.html')