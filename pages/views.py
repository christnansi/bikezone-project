from django.shortcuts import render
from pages.models import Teams
from bikes.models import Bike

# Create your views here.
def home(request):
    teams = Teams.objects.all()
    featured_bikes = Bike.objects.order_by('-created_date').filter(is_featured=True) 
    all_bikes = Bike.objects.order_by('-created_date')
    context = {
        'teams' : teams,
        'featured_bikes' : featured_bikes,
        'all_bikes' : all_bikes,
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
