from django.urls import path
from .views import index, places, PlaceCreate


urlpatterns = [
    path('', index, name='index'),
    path('places/',places, name='places'),
    path('create/', PlaceCreate.as_view(), name='create'),
    ]