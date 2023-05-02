from django.shortcuts import render
from .models import FLight

# Create your views here.
def index(request):
    return render(request, "flights/index.html", {
        "flights": FLight.objects.all()
    })