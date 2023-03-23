from django import forms


class GraphInputForm(forms.Form):
    graph_input = forms.CharField(label='Graph Data:', widget=forms.Textarea)


class RandomGraphForm(forms.Form):
    node_count = forms.IntegerField(label='Node Count:')
    edge_count = forms.IntegerField(label='Edge Count:')

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data['node_count'] < 0:
            raise forms.ValidationError('Node count must be greater than 0.')
        if cleaned_data['edge_count'] < 0:
            raise forms.ValidationError('Edge count must be greater than 0.')
        return cleaned_data