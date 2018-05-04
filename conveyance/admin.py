from django.contrib import admin
from .models import cities,vehicles,renting

admin.site.register(cities)
admin.site.register(vehicles)
admin.site.register(renting)