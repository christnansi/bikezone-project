from . import views
from django.urls import path

urlpatterns = [
    path('', views.bikes, name="bikes"),
    path('<int:id>', views.bike_detail, name="bike_detail"),
    
]