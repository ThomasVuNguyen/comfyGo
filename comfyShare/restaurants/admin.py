from django.contrib import admin

# Register your models here.
from .models import Restaurant

class RestaurantAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,  {'fields': ['name']}),
        (None,  {'fields': ['addresses']}),
        (None,  {'fields': ['latitude']},),
        (None,  {'fields': ['longtitude']}),
    ]
    list_display = ('name', 'address','latitude', 'longitude')
admin.site.register(Restaurant, RestaurantAdmin)