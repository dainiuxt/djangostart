from django.shortcuts import render
from .models import CarModel, Car, Order, OrderRow, Service
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.db.models import Q
from django.core.paginator import Paginator

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
    # cars = Car.objects.all()
    paginator = Paginator(Car.objects.all(), 2)
    page_number = request.GET.get('page')
    paged_cars = paginator.get_page(page_number)
    context = {
        'cars': paged_cars
    }
    # print(cars)
    return render(request, 'servisiux/cars.html', context=context)

def car(request, car_id):
    single_car = get_object_or_404(Car, pk = car_id)
    # car_orders = Order.objects.get()
    return render(request, 'servisiux/car.html', {'car': single_car})

class OrderListView(generic.ListView):
    model = Order
    paginate_by = 5
    template_name = 'servisiux/order_list.html'

class OrderDetailView(generic.DetailView):
    model = Order
    template_name = 'servisiux/order_detail.html'

def search(request):
    """
    paprasta paieška. query ima informaciją iš paieškos laukelio,
    search_results prafiltruoja pagal įvestą tekstą knygų pavadinimus ir aprašymus.
    Icontains nuo contains skiriasi tuo, kad icontains ignoruoja ar raidės 
    didžiosios/mažosios.
    """
    query = request.GET.get('query')
    search_results = Car.objects.filter(Q(model_id__make__icontains=query) | Q(owner__icontains=query))
    return render(request, 'servisiux/search.html', {'cars': search_results, 'query': query})
