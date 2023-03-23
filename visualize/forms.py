from django import forms


class GraphInputForm(forms.Form):
    graph_input = forms.CharField(label='Graph Data:', widget=forms.Textarea)

#    def clean(self):
#        cleaned_data = super().clean()
#        if len(cleaned_data['graph_input'].split()) % 2 != 0:
#            raise forms.ValidationError('Invalid input data.')
#        return cleaned_data


class RandomGraphForm(forms.Form):
    node_count = forms.IntegerField(label='Node Count:')
    probability = forms.FloatField(label='Probability for Edge Creation:')

#    def clean(self):
#        cleaned_data = super().clean()
#        if cleaned_data['node_count'] < 0:
#            raise forms.ValidationError('Node count must be greater than 0.')
#        if cleaned_data['probability'] < 0 or cleaned_data['probability'] > 1:
#            raise forms.ValidationError('Probability must be between 0 ans 1.')
#        return cleaned_data