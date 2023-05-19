from django import forms


TYPE_CHOICES = (
    ('input', 'Input'),
    ('file', 'File'),
    ('example', 'Example'),
    ('generate', 'Generate'),
    )

EXAMPLE_CHOICES = (
    ('karate_club', "Zachary's karate club"),
    ('davis_southern_women', "Davis' Southern women social network"),
    ('florentine_families', 'Florentine families network'),
    ('les_miserables', 'Characters in the novel Les Miserables'),
    )

GRAPH_CHOICES = (
    ('graph', 'Undirected Graph'),
    ('digraph', 'Directed Graph'),
    )
METHOD_CHOICES = (
    # networkx
    ('greedy_modularity_maximization', 'Greedy Modularity Maximization'),
    ('louvain_community_detection', 'Louvain Community Detection'),
    ('label_propagation', 'Label Propagation'),
    ('asynchronous_label_propagation', 'Asynchronous Label Propagation'),
    # karateclub
    ('karateclub_GEMSEC', 'GEMSEC'),
    ('karateclub_EdMot', 'EdMot'),
    ('karateclub_SCD', 'SCD'),
    # custom
    ('custom', 'Custom'),
    )
LAYOUT_CHOICES = (
    ('spring', 'spring'),
    ('circular', 'circular'),
    ('kamada_kawai', 'Kamada-Kawai'),
    ('shell', 'shell'),
    ('planar', 'planar'),
    ('spiral', 'spiral'),
    )

METHOD_UNWEIGHTED = (
    'label_propagation'
    )

class GraphVizForm(forms.Form):
    input_type = forms.ChoiceField(
        label='Input Type:', choices=TYPE_CHOICES, disabled=False)

    # input
    graph_input_text = forms.CharField(
        label='Graph Data:', widget=forms.Textarea, required=False)
    # file
    graph_input_file = forms.FileField(
        label='Graph File:', widget=forms.ClearableFileInput, required=False)
    # input & file
    graph_type = forms.ChoiceField(
        label='Graph Type:', choices=GRAPH_CHOICES, required=False)
    graph_weighted = forms.BooleanField(label='is weighted', required=False)
    # example
    graph_input_example = forms.ChoiceField(
        label='Example Name:', choices=EXAMPLE_CHOICES, required=False)
    # generate
    generate_arg_n = forms.IntegerField(label='n', required=False)
    generate_arg_k = forms.IntegerField(label='k', required=False)
    generate_arg_p = forms.FloatField(label='p', required=False)
    generate_arg_seed = forms.IntegerField(label='seed', required=False)

    methods = forms.MultipleChoiceField(
        label='Methods Selected:', choices=METHOD_CHOICES,
        widget=forms.CheckboxSelectMultiple)
    layout = forms.ChoiceField(
        label='Layout Selected:', choices=LAYOUT_CHOICES)
    custom_code = forms.FileField(
        label='', widget=forms.ClearableFileInput(attrs={'multiple': True}),
        required=False,
        help_text='related files when <i>Custom</i> is selected, and main.* is needed.')

    def clean(self):
        cleaned_data = super().clean()

        # TODO: form check
        # print('cleaned_data: ', cleaned_data)
        #
        # is_weighted = cleaned_data['graph_weighted']
        # method_list = cleaned_data['methods']
        #
        # if is_weighted:
        #     if len(cleaned_data['graph_input'].split()) % 3 != 0:
        #         raise forms.ValidationError('Invalid graph data.')
        #     invalid_methods = []
        #     for method in method_list:
        #         if method in METHOD_UNWEIGHTED:
        #             invalid_methods.append(method)
        #     if len(invalid_methods) > 0:
        #         message = ''
        #         for method in invalid_methods:
        #             message += "'" + method.replace('_', ' ').title() + "'"
        #         message += 'can only be used in an unweighted graph.'
        #         raise forms.ValidationError(message)
        # else:
        #     if len(cleaned_data['graph_input'].split()) % 2 != 0:
        #         raise forms.ValidationError('Invalid graph data.')
        return cleaned_data