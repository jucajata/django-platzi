from django.views.generic.base import TemplateView
from django import views
from django.http import HttpResponse
from django.shortcuts import render
from .models import Car, Author, Profile

# Create your views here.
def my_view(request):
    car_list = Car.objects.all()
    context = {
        "car_list": car_list
    }
    return render(request, "my_first_app/car_list.html", context)


class CarListView(TemplateView):
    template_name = "my_first_app/car_list.html"
    
    def get_context_data(self):
        car_list = Car.objects.all()
        return {
            "car_list": car_list
        }

def my_test_view(request, *args, **kwargs):
    print(args)
    print(kwargs)
    return HttpResponse("")

def author_view(request, *args, **kwargs):
    print(args)
    print(kwargs)
    try:
        author = Author.objects.get(id=kwargs['id'])
        try:
            profile = Profile.objects.get(author_id=kwargs['id'])
            return HttpResponse(f"Author: {author.name} - Website: {profile.website} - Biografia: {profile.biography} ")
        except Profile.DoesNotExist:
            return HttpResponse(f"Author: {author.name}")
    except Author.DoesNotExist:
        return HttpResponse("El autor no existe")