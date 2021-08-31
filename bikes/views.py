from django.shortcuts import get_object_or_404, render
from bikes.models import Bike
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# Create your views here.

def bikes(request):
    all_bikes = Bike.objects.order_by('-created_date')
    paginator = Paginator(all_bikes, 2)
    page = request.GET.get('page')
    paged_bikes = paginator.get_page(page) 

    model_search = Bike.objects.values_list('model', flat=True).distinct()
    city_search = Bike.objects.values_list('city', flat=True).distinct()
    year_search = Bike.objects.values_list('year', flat=True).distinct()
    body_type_search = Bike.objects.values_list('body_type', flat=True).distinct()

    context={
        'all_bikes' : paged_bikes,
        'model_search': model_search,
        'city_search': city_search,
        'year_search': year_search,
        'body_type_search': body_type_search,
    }
    return render(request, 'bikes/bikes.html', context)


def bike_detail(request, id):
    single_bike = get_object_or_404(Bike, pk=id)

    context = {
        'single_bike' : single_bike,
    }
    return render(request, "bikes/bike_detail.html", context)


def search(request):
    bikes = Bike.objects.order_by('-created_date')

    model_search = Bike.objects.values_list('model', flat=True).distinct()
    city_search = Bike.objects.values_list('city', flat=True).distinct()
    year_search = Bike.objects.values_list('year', flat=True).distinct()
    body_type_search = Bike.objects.values_list('body_type', flat=True).distinct()
    transmission_search = Bike.objects.values_list('transmission', flat=True).distinct()

    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword :
            bikes = bikes.filter(description__icontains=keyword)

    if 'model' in request.GET:
        model = request.GET['model']
        if model:
            bikes = bikes.filter(model__iexact=model)

    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            bikes = bikes.filter(city__iexact=city)

    if 'year' in request.GET:
        year = request.GET['year']
        if year:
            bikes = bikes.filter(year__iexact=year)

    if 'transmission' in request.GET:
        transmission = request.GET['transmission']
        if transmission:
            bikes = bikes.filter(transmission__iexact=transmission)

    if 'body_type' in request.GET:
        body_type = request.GET['body_type']
        if body_type:
            bikes = bikes.filter(body_type__iexact=body_type)

    if 'min_price' in request.GET:
        min_price = request.GET['min_price']
        max_price = request.GET['max_price']
        if max_price:
            bikes = bikes.filter(price__gte=min_price, price__lte=max_price)

    context = {
        'bikes' : bikes,
        'model_search': model_search,
        'city_search': city_search,
        'year_search': year_search,
        'body_type_search': body_type_search,
        'transmission_search' : transmission_search,
    }
    return render(request, "bikes/search.html", context)
