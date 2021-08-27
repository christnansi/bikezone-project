from bikes.models import Bike
from django.contrib import admin
from django.utils.html import format_html

# Register your models here.

class BikeAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40"/>'.format(object.bike_photo.url))

    thumbnail.short_description = 'Bike Image'

    list_display = ('id', 'thumbnail', 'bike_title','city', 'color', 'model', 'body_type', 'fuel_capacity', 'is_featured')
    list_display_links = ('id', 'thumbnail', 'bike_title')
    list_editable = ('is_featured',)
    search_fields = ('id', 'bike_title', 'city', 'model', 'body_type',)
    list_filter = ('city', 'model', 'body_type')

admin.site.register(Bike, BikeAdmin)
