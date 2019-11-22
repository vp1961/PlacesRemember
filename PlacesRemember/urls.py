from django.urls import path
from .views import index, places, PlaceCreate, place_detail


urlpatterns = [
    path('', index, name='index'),
    path('places/',places, name='places'),
    path('create/', PlaceCreate.as_view(), name='create'),
    path('place/<str:id>/', place_detail, name='place_detail'),
    ]