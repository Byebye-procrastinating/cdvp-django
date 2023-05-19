from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('features', views.features, name='features'),
    path('application', views.application, name='application'),
    path('about', views.about, name='about'),

    path('api/example', views.example, name='example'),
    path('api/generate/newman_watts_strogatz',
         views.generate_newman_watts_strogatz,
         name='generate_newman_watts_strogatz'),
    path('api/visualize', views.visualize, name='visualize'),
]