from django.shortcuts import render, get_object_or_404, reverse, redirect
from .models import CarModel, Car, Order, OrderRow, Service
from django.views.generic import (
                                ListView,
                                DetailView,
                                DeleteView,
                                CreateView,
                                UpdateView,
                                )
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.forms import User
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
from .forms import OrderForm, OrderReviewForm, UserUpdateForm, ProfileUpdateForm
from django.views.generic.edit import FormMixin
from django.contrib.auth.decorators import login_required
from datetime import date

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

class OrderListView(ListView):
    model = Order
    paginate_by = 5
    template_name = 'servisiux/order_list.html'

class OrderDetailView(FormMixin, DetailView):
    model = Order
    template_name = 'servisiux/order_detail.html'
    form_class = OrderReviewForm

    class Meta:
        ordering = ['title']

    def get_success_url(self):
        return reverse('order-detail', kwargs={'pk': self.object.id})

    def get_context_data(self, *args, **kwargs):
       context = super(OrderDetailView, self).get_context_data(**kwargs)
       context['form'] = OrderReviewForm(initial={'order': self.object})
       return context   

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.instance.order = self.object
        form.instance.reviewer = self.request.user
        form.save()
        return super(OrderDetailView, self).form_valid(form)

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

class UserOrdersListView(LoginRequiredMixin, ListView):
    model = Order
    template_name ='servisiux/user_orders.html'
    paginate_by = 10
    
    def get_queryset(self):
        return Order.objects.filter(user=self.request.user).order_by('due_date')

@csrf_protect
def register(request):
    if request.method == "POST":
        # pasiimame reikšmes iš registracijos formos
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        # tikriname, ar sutampa slaptažodžiai
        if password == password2:
            # tikriname, ar neužimtas username
            if User.objects.filter(username=username).exists():
                messages.error(request, f'Vartotojo vardas {username} užimtas!')
                return redirect('register')
            else:
                # tikriname, ar nėra tokio pat email
                if User.objects.filter(email=email).exists():
                    messages.error(request, f'Vartotojas su el. paštu {email} jau užregistruotas!')
                    return redirect('register')
                else:
                    # jeigu viskas tvarkoje, sukuriame naują vartotoją
                    User.objects.create_user(username=username, email=email, password=password)
        else:
            messages.error(request, 'Slaptažodžiai nesutampa!')
            return redirect('register')
    return render(request, 'registration/register.html')

@login_required
def profile(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f"Profile updated")
            return redirect('servisiux/profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
    }    
    return render(request, 'servisiux/profile.html', context)

class UserOrders(LoginRequiredMixin, ListView):
    model = Order
    context_object_name = 'orders'
    template_name = 'servisiux/my_orders.html'
    paginate_by = 10

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user).order_by('due_date')

class UserOrdersDetail(LoginRequiredMixin, DetailView):
    model = Order
    template_name = 'servisiux/my_order.html'

class UserOrderCreateView(LoginRequiredMixin, CreateView):
    model = Order
    form_class = OrderForm

    success_url = "/servisiux/userorders/"
    template_name = 'servisiux/my_order_new.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.date = date.today()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'].fields['car_instance_id'].queryset = Car.objects.filter(own_id=self.request.user)
        return context


class UserOrderUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Order
    form_class = OrderForm

    success_url = "/servisiux/userorders/"
    template_name = 'servisiux/my_order_new.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.date = date.today()
        return super().form_valid(form)

    def form_valid(self, form):
        form.instance.reader = self.request.user
        return super().form_valid(form)

    def test_func(self):
        order = self.get_object()
        return self.request.user == order.user

