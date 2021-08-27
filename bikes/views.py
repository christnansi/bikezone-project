from django.shortcuts import render

# Create your views here.

def bikes(request):
    return render(request, 'bikes/bikes.html')


def bike_detail(request, id):
    return render(request, "bikes/bike_detail.html")