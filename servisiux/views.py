from operator import mod
from django.shortcuts import render
from django.http import HttpResponse
from pytest import Session
from .models import CarModel, Car, Order, OrderRow, Service
from django.shortcuts import render, get_object_or_404
from django.views import generic

# Create your views here.
def index(request):
    return render(request, 'servisiux/index.html')

def stats(request):
    qty_services = Service.objects.all().count()
    qty_orders = Order.objects.all().count()
    qty_cars = Car.objects.all().count()
    qty_models = CarModel.objects.all().count()

    context = {
        'qty_serv': qty_services,
        'qty_orders': qty_orders,
        'qty_cars': qty_cars,
        'qty_models': qty_models,
    }
    return render(request, 'servisiux/stats.html', context=context)

def cars(request):
    cars = Car.objects.all()
    context = {
        'cars': cars
    }
    # print(cars)
    return render(request, 'servisiux/cars.html', context=context)

def car(request, car_id):
    single_car = get_object_or_404(Car, pk = car_id)
    return render(request, 'servisiux/car.html', {'car': single_car})

class OrderListView(generic.ListView):
    model = Order
    template_name = 'servisiux/order_list.html'

class OrderDetailView(generic.DetailView):
    model = Order
    template_name = 'servisiux/order_detail.html'
