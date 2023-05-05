from django.contrib import admin
from .models import Flight, Airport, Passenger
# Register your models here.

admin.site.register(Airport)
admin.site.register(Flight) # This will add the Flight model to the admin page.
admin.site.register(Passenger) # This will add the Passenger model to the admin page.