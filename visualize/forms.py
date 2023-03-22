from django import forms


class GraphInputForm(forms.Form):
    graph_input = forms.CharField(label='Graph Input', widget=forms.Textarea)