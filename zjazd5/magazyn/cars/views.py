from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from cars.model

from zjazd5.magazyn.cars.models import Cars


def hello_world_name


def cars_list(request):
    cars = Cars.objects.all()
    output = ""
    for cars in cars:
        output += f'(cars.id)  <a href="/cars/(cars.id">(cars.name)</a><hr>'
        return HttpResponse(output)

    def products_list(request):
        product = Cars.objects.all()
        return render(
            request = request
            context =('cars')
