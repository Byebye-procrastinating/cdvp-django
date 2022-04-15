from django.shortcuts import render
import networkx as nx

from .models import GraphInput
from .forms import GraphInputForm
from .visualization import visualize


def index(request):
    graph_svg = ''

    if request.method != 'POST':
        form = GraphInputForm()
    else:
        form = GraphInputForm(request.POST)
        if form.is_valid():
            GraphInput = form.save(commit=False)

            G = nx.Graph(NodeList=[1, 2, 3])
            edge_list = str(GraphInput.graph_data).split()
            ne = len(edge_list)
            for i in range(0, ne, 2):
                u, v = int(edge_list[i]), int(edge_list[i + 1])
                G.add_edge(u, v)
            visualize(G, 'output.svg')
            with open('output.svg', 'r') as f_obj:
                graph_svg = f_obj.read()

    content = {'form': form, 'graph_svg': graph_svg }
    return render(request, 'visualize/index.html', content)