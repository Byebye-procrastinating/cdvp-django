from django import forms


METHOD_CHOICES = (
    ('greedy_modularity_maximization', 'Greedy Modularity Maximization'),
    ('louvain_community_detection', 'Louvain Community Detection'),
    ('label_propagation', 'Label Propagation'),
    )
LAYOUT_CHOICES = (
    ('spring', 'spring'),
    ('random', 'random'),
    )

class GraphVizForm(forms.Form):
    graph_input = forms.CharField(label='Graph Data:', widget=forms.Textarea)
    methods = forms.MultipleChoiceField(
        label='Methods Selected:', choices=METHOD_CHOICES, widget=forms.CheckboxSelectMultiple)
    layout = forms.ChoiceField(
        label='Layout Selected:', choices=LAYOUT_CHOICES)

    def clean(self):
        cleaned_data = super().clean()
        if len(cleaned_data['graph_input'].split()) % 2 != 0:
            raise forms.ValidationError('Invalid input data.')
        return cleaned_data