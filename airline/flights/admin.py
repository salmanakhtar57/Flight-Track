from django.contrib import admin
from .models import Flight, Airport, Passenger
# Register your models here.

class FlightAdmin(admin.ModelAdmin):
    list_display = ("id", "origin", "destination", "duration")

class PassengerAdmin(admin.ModelAdmin):
    filter_horizontal = ("flights",)

admin.site.register(Airport)
admin.site.register(Flight) # This will add the Flight model to the admin page.
admin.site.register(Passenger) # This will add the Passenger model to the admin page.