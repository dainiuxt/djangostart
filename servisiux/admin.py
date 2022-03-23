from django.contrib import admin
from .models import CarModel, Car, Order, OrderRow, Service
# Register your models here.

admin.site.register(CarModel)
admin.site.register(Car)
admin.site.register(Order)
admin.site.register(OrderRow)
admin.site.register(Service)