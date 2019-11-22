from django.shortcuts import render
from .forms import PlaceForm
from django.views.generic import View
from django.shortcuts import redirect

def index(request):
    return render(request,'PlacesRemember/index.html')


def places(request):
    return render(request,'PlacesRemember/places.html')

class PlaceCreate(View):
    def get(self, request):
        place_form = PlaceForm()
        print(request.user)

        return render(
            request, 'PlacesRemember/place_create.html', 
            context={'place_form': place_form})

    def post(self, request):
        bound_place_form = PlaceForm(request.POST)
        user = request.user

        if bound_place_form.is_valid():
            new_place = bound_place_form.save(user)

            return redirect('/places/', permanent=True)
        return render(
            request, 
            'PlacesRemember/place_create.html',
            context={'place_form': bound_place_form})