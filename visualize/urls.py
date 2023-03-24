from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('features', views.features, name='features'),
    path('application', views.application, name='application'),
    path('about', views.about, name='about'),

    path('generate', views.generate, name='generate'),
]