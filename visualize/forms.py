from django import forms


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
    graph_input = forms.CharField(label='Graph Data:', widget=forms.Textarea)
    graph_type = forms.ChoiceField(label='Graph Type:', choices=GRAPH_CHOICES)
    graph_weighted = forms.BooleanField(label='is weighted', required=False)
    methods = forms.MultipleChoiceField(
        label='Methods Selected:', choices=METHOD_CHOICES, widget=forms.CheckboxSelectMultiple)
    layout = forms.ChoiceField(
        label='Layout Selected:', choices=LAYOUT_CHOICES)

    def clean(self):
        cleaned_data = super().clean()
        is_weighted = cleaned_data['graph_weighted']
        method_list = cleaned_data['methods']

        if is_weighted:
            if len(cleaned_data['graph_input'].split()) % 3 != 0:
                raise forms.ValidationError('Invalid graph data.')
            invalid_methods = []
            for method in method_list:
                if method in METHOD_UNWEIGHTED:
                    invalid_methods.append(method)
            if len(invalid_methods) > 0:
                message = ''
                for method in invalid_methods:
                    message += "'" + method.replace('_', ' ').title() + "'"
                message += 'can only be used in an unweighted graph.'
                raise forms.ValidationError(message)
        else:
            if len(cleaned_data['graph_input'].split()) % 2 != 0:
                raise forms.ValidationError('Invalid graph data.')
        return cleaned_data