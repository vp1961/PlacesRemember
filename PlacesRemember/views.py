from django.shortcuts import render

def index(request):
    return render(request,'PlacesRemember/index.html')


def places(request):
    return render(request,'PlacesRemember/places.html')