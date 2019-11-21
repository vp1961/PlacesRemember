from django.urls import path
from .views import index,places


urlpatterns = [
    path('', index, name='index'),
    path('places/',places, name='places')
    ]