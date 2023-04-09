from django.urls import path

from . import views


urlpatterns = [
    path('example', views.example, name='example'),
    path('generate/newman_watts_strogatz',
         views.generate_newman_watts_strogatz,
         name='generate_newman_watts_strogatz'),
    path('visualize', views.visualize, name='visualize'),
]