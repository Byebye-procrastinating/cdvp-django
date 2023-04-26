import json, os, time
import re

from django.core.files.storage import default_storage
from django.http import JsonResponse
from django.shortcuts import render
import karateclub.community_detection.non_overlapping as kc_com_n
import networkx as nx
import networkx.algorithms.community as nx_com

from .forms import GraphVizForm
from .visualization import graph_viz, size_distribution
from .docker_engine.docker_eni import get_output
from datetime import datetime

def easy_asyn_lpa_communities(G, weight=None, seed=None):
    community_set = []
    community_gen = nx_com.asyn_lpa_communities(G, weight, seed)
    for community in community_gen:
        community_set.append(community)
    return community_set

# 根据 algorithm_name 得到对应算法
def choose_algo(graph, is_weighted, algorithm_name):
    ALGORITHMS = {
        'greedy_modularity_maximization': nx_com.greedy_modularity_communities,
        'louvain_community_detection': nx_com.louvain.louvain_communities,
        'label_propagation': nx_com.label_propagation_communities,
        'asynchronous_label_propagation': easy_asyn_lpa_communities,
    }
    if algorithm_name not in ALGORITHMS:
        raise RuntimeError('no method named ' + algorithm_name)
    algo = ALGORITHMS[algorithm_name]
    if is_weighted:
        return algo(graph, weight='weight')
    return algo(graph)


def choose_karateclub_algo(graph, model_name):
    MODELS = {
        'GEMSEC': kc_com_n.GEMSEC(),
        'EdMot': kc_com_n.EdMot(),
        'SCD': kc_com_n.SCD(),
    }
    if model_name not in MODELS:
        raise RuntimeError('no model named ' + model_name)
    model = MODELS[model_name]
    model.fit(graph)
    memberships = model.get_memberships()
    community_set = {}
    for x, com in memberships.items():
        try:
            community_set[com].append(x)
        except:
            community_set[com] = [x]
    return [frozenset(l) for l in community_set.values()]


# 根据 layout_name 得到对应布局方式
def choose_layout(layout_name):
    LAYOUTS = {
        'spring': nx.spring_layout,
        'circular': nx.circular_layout,
        'kamada_kawai': nx.kamada_kawai_layout,
        'shell': nx.shell_layout,
        'planar': nx.planar_layout,
        'spiral': nx.spiral_layout,
    }
    if layout_name not in LAYOUTS:
        raise RuntimeError('no layout named ' + layout_name)
    return LAYOUTS[layout_name]

# 根据 graph_type 得到图的类型
def choose_graph(graph_type):
    TYPES = {
        'graph': nx.Graph(),
        'digraph': nx.DiGraph(),
    }
    if graph_type not in TYPES:
        raise RuntimeError('no graph type named ' + graph_type)
    return TYPES[graph_type]

# 根据 layout 和 methods 的设置对 graph 施以可视化
def process_methods(graph, layout, methods, is_weighted, filepath = ''):
    graph = nx.convert_node_labels_to_integers(graph)

    layout_algo = choose_layout(layout)
    results = []
    for method in methods:
        current = {}

        if method == 'custom':
            community_set = get_output(filepath)
            current['method'] = 'Custom'
        elif 'karateclub' in method:
            formed_method = method.split('_', 1)[-1]
            community_set = choose_karateclub_algo(
                graph.copy(), formed_method)
            current['method'] = formed_method.replace('_', ' ')
        else:
            community_set = choose_algo(graph, is_weighted, method)
            current['method'] = method.replace('_', ' ').title()

        current['modularity'] = nx_com.quality.modularity(graph, community_set)
        current['coverage'], current['performance'] = \
            nx_com.quality.partition_quality(graph, community_set)
        current['graph_viz'] = graph_viz(
            graph, community_set, layout_algo).getvalue()
        current['size_distribution'] = size_distribution(
            community_set).getvalue()

        results.append(current)
    return results


def visualize(request):
    if request.method == 'POST':
        path = ""
        data = request.POST

        config = json.loads(data['config'])
        methods, layout = config['methods'], config['layout']

        graph_data = json.loads(data['graph_data'])

        type = data['type']
        if type == 'input':
            is_weighted = graph_data['weighted']
            graph = choose_graph(graph_data['graph_type'])

            edge_list = graph_data['edge_list']
            if is_weighted:
                graph.add_weighted_edges_from(edge_list)
            else:
                graph.add_edges_from(edge_list)
        elif type == 'file':
            is_weighted = graph_data['weighted']
            graph = choose_graph(graph_data['graph_type'])

            edge_list = request.FILES.get('edge_list').read().split()
            ne = len(edge_list)
            if is_weighted:
                for i in range(0, ne, 3):
                    u, v, w = [int(val) for val in edge_list[i:i+3]]
                    graph.add_edge(u, v, weight=w)
            else:
                for i in range(0, ne, 2):
                    u, v = [int(val) for val in edge_list[i:i+2]]
                    graph.add_edge(u, v)
        elif type == 'example':
            is_weighted = False
            graph = get_example(graph_data['name'])
        elif type == 'generate':
            n, k, p = graph_data['n'], graph_data['k'], graph_data['p']
            seed = None
            if 'seed' in graph_data:
                seed = graph_data['seed']
            is_weighted = False
            graph = nx.generators.random_graphs.newman_watts_strogatz_graph(
                n, k, p, seed)
        else:
            return JsonResponse()

        if 'custom' in methods:
            file_list = request.FILES.getlist('code')
            # TODO:  更改文件夹名 hash_code
            now = str(datetime.now()).replace(' ', '_').replace('.', '_').replace(':', '_')
            path = (os.path.abspath('.') + '/' + now).replace('\\', '/')
            for file in file_list:
                default_storage.save(path + '/' + file.name, file)

            pattern = re.compile(r"^main\.\w+$")

            main_files = []
            for file in file_list:
                if pattern.match(file.name):
                    main_files.append(file.name)

            if len(main_files) > 1:
                raise Exception("Multiple 'main' files found: {}".format(main_files))

            if len(main_files) == 0:
                raise Exception("No 'main' file found.")
            filepath = path + '/' +main_files[0]

            with default_storage.open(path + '/' + 'dataset', 'w') as f:
                if is_weighted:
                    weights = nx.get_edge_attributes(graph, 'weight')
                    for edge in graph.edges:
                        f.write(str(edge[0]) + ' ' + str(edge[1]) + str(weights[edge]) + '\n')
                else:
                    for edge in graph.edges:
                        f.write(str(edge[0]) + ' ' + str(edge[1]) + '\n')
            default_storage.save(path + '/' + 'dataset', f)

        content = {
            'results': process_methods(graph, layout, methods, is_weighted, filepath),
            }
        return JsonResponse(content)


def get_example(network_name):
    EXAMPLES = {
        'karate_club': nx.karate_club_graph(),
        'davis_southern_women': nx.davis_southern_women_graph(),
        'florentine_families': nx.florentine_families_graph(),
        'les_miserables': nx.les_miserables_graph(),
    }
    if network_name not in EXAMPLES:
        raise RuntimeError('no example named ' + network_name)
    graph = EXAMPLES[network_name]
    return nx.convert_node_labels_to_integers(graph)

# 根据请求选择样例
def example(request):
    if request.method == 'GET':
        graph_json = {
            'graph_type': 'graph',
            'weighted': False,
            'edge_list': list(get_example(request.GET['q']).edges),
        }
        return JsonResponse(graph_json)


# 根据输入生成对应 Newman–Watts–Strogatz small-world 图
def generate_newman_watts_strogatz(request):
    if request.method == 'GET':
        n, k = int(request.GET['n']), int(request.GET['k'])
        p = float(request.GET['p'])
        seed = None
        if 'seed' in request.GET:
            seed = int(request.GET['seed'])
        content = {
            "graph_data": "graph",
            "weighted": False,
            "edge_list":
                list(nx.generators.random_graphs.newman_watts_strogatz_graph(
                    n, k, p, seed).edges),
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

            graph = choose_graph(form.cleaned_data['graph_type'])
            edge_list = form.cleaned_data['graph_input'].split()
            is_weighted = form.cleaned_data['graph_weighted']

            ne = len(edge_list)
            if is_weighted:
                for i in range(0, ne, 3):
                    u, v, w = [int(val) for val in edge_list[i:i+3]]
                    graph.add_edge(u, v, weight=w)
            else:
                for i in range(0, ne, 2):
                    u, v = [int(val) for val in edge_list[i:i+2]]
                    graph.add_edge(u, v)

            results = process_methods(graph, layout, methods, is_weighted)

    content = {
        'form_graph_input': form,
        'results': results,
        }
    return render(request, 'visualize/application.html', content)

def about(request):
    return render(request, 'visualize/about.html')