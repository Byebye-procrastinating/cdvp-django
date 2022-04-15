from django.db import models


class GraphInput(models.Model):
    """
    User's input to describe a graph
    """
    graph_data = models.TextField()