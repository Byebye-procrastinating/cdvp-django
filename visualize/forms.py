from django import forms


class GraphInputForm(forms.Form):
    graph_input = forms.CharField(label='Graph Data:', widget=forms.Textarea)

    def clean(self):
        cleaned_data = super().clean()
        if len(cleaned_data['graph_input'].split()) % 2 != 0:
            raise forms.ValidationError('Invalid input data.')
        return cleaned_data