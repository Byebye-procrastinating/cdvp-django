from django import forms

from .models import GraphInput


class GraphInputForm(forms.ModelForm):
    class Meta:
        model = GraphInput
        fields = ['graph_data']
        labels = {'graph_data': ''}