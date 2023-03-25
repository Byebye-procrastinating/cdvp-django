import io, json

from django.http import JsonResponse
from django.shortcuts import render
import networkx as nx
import networkx.algorithms.community as nx_com

from .forms import GraphVizForm
from .visualization import graph_viz, size_distribution, calc_modularity


# 根据 algorithm_name 得到对应算法
def choose_algo(algorithm_name):
    if algorithm_name == 'greedy_modularity_maximization':
        return nx_com.greedy_modularity_communities
    if algorithm_name == 'louvain_community_detection':
        return nx_com.louvain.louvain_communities
    if algorithm_name == 'label_propagation':
        return nx_com.label_propagation_communities

# 根据 layout_name 得到对应布局方式
def choose_layout(layout_name):
    if layout_name == 'spring':
        return nx.spring_layout
    if layout_name == 'random':
        return nx.random_layout

# 根据 graph_type 得到图的类型
def choose_graph(graph_type):
    if graph_type == 'graph':
        return nx.Graph()
    if graph_type == 'digraph':
        return nx.DiGraph()
    if graph_type == 'multigraph':
        return nx.MultiGraph()
    if graph_type == 'multidigraph':
        return nx.MultiDiGraph()

# 根据 layout 和 methods 的设置对 graph 施以可视化
def process_methods(graph, layout, methods):
    layout_algo = choose_layout(layout)
    results = []
    for method in methods:
        callable_method = choose_algo(method)
        current = {}
        current['method'] = method.replace('_', ' ').title()
        current['modularity'] = calc_modularity(graph, callable_method)
        current['graph_viz'] = graph_viz(
            graph, callable_method, layout_algo).getvalue()
        current['size_distribution'] = size_distribution(
            graph, callable_method).getvalue()

        results.append(current)
    return results


# 根据 config 的格式限制和 graph_data 的数据得到图的可视化结果
def visualize(request):
    if request.method == 'POST':
        req = json.loads(request.body)
        config = req.get('config')
        graph_data = req.get('graph_data')
        
        methods = config['methods']
        layout = config['layout']
        # TODO: 支持多种类型的图
        # graph = choose_graph(graph_data['graph_type'])
        graph = nx.Graph()
        if graph_data['weighted']:
            graph.add_weighted_edges_from(graph_data['edge_list'])
        else:
            graph.add_edges_from(graph_data['edge_list'])

        content = {
            'results': process_methods(graph, layout, methods),
            }
        return JsonResponse(content)


# TODO: 根据输入生成满足对应要求的图
def generate(request):
    if request.method == 'GET':
        content = {
            "graph_data": "graph",
            "weighted": False,
            "edge_list": [
                [1, 2],
                [3, 4],
            ]
            }
        return JsonResponse(content)


def index(request):
    return render(request, 'visualize/index.html')

def features(request):
    return render(request, 'visualize/features.html')

def application(request):
    results = {}

    if request.method != 'POST':
        form = GraphVizForm()
    else:
        form = GraphVizForm(request.POST)
        if form.is_valid():
            methods = form.cleaned_data['methods']
            layout = form.cleaned_data['layout']
            graph = nx.Graph()
            edge_list = form.cleaned_data['graph_input'].split()
            ne = len(edge_list)
            for i in range(0, ne, 2):
                u, v = int(edge_list[i]), int(edge_list[i + 1])
                graph.add_edge(u, v)

            results = process_methods(graph, layout, methods)

    content = {
        'form_graph_input': form,
        'results': results,
        }
    return render(request, 'visualize/application.html', content)

def about(request):
    return render(request, 'visualize/about.html')