from pages.models import Teams
from django.shortcuts import render

# Create your views here.
def home(request):
    teams = Teams.objects.all()
    context = {
        'teams' : teams,
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