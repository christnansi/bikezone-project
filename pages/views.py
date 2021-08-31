from django.shortcuts import render
from pages.models import Teams
from bikes.models import Bike

# Create your views here.
def home(request):
    teams = Teams.objects.all()
    featured_bikes = Bike.objects.order_by('-created_date').filter(is_featured=True) 
    all_bikes = Bike.objects.order_by('-created_date')

    model_search = Bike.objects.values_list('model', flat=True).distinct()
    city_search = Bike.objects.values_list('city', flat=True).distinct()
    year_search = Bike.objects.values_list('year', flat=True).distinct()
    body_type_search = Bike.objects.values_list('body_type', flat=True).distinct()

    context = {
        'teams' : teams,
        'featured_bikes' : featured_bikes,
        'all_bikes' : all_bikes,
        'model_search' : model_search,
        'city_search' : city_search,
        'year_search' : year_search,
        'body_type_search' : body_type_search,
    }
    return render(request, "pages/home.html", context)

def about(request):
    teams = Teams.objects.all()
    context = {
        'teams' : teams,
    }
    return render(request, "pages/about.html", context)

def services(request):
    return render(request, "pages/services.html")

def contact(request):
    return render(request, "pages/contact.html")
