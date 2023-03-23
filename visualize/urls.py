from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('', views.generate_random_graph, name='generate_random_graph'),
    path('features', views.features, name='features'),
    path('about', views.about, name='about'),
]