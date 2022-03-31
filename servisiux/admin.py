from django.contrib import admin
from .models import CarModel, Car, Order, OrderRow, Service

# Register your models here.

class OrderRowAdmin(admin.ModelAdmin):
    list_display = ('service_id', 'order_id', 'quantity')

class OrderRowInline(admin.TabularInline):
  model = OrderRow
  readonly_fields = ('id',)
  can_delete = False
  extra = 0

class OrderInline(admin.TabularInline):
  model = Order
  list_display = ('date', 'car_instance_id',)
  list_display_links = ('id',)  
  show_change_link = True
  readonly_fields = ('date',)
  can_delete = False
  extra = 0


class OrderAdmin(admin.ModelAdmin):
  list_display = ('date', 'car_instance_id',)
  list_display_links = ('date',)
  inlines = [OrderRowInline]

  fieldsets = (
    ('Order', {
      'fields': ('date', 'car_instance_id', 'status',) 
    }),
    ('User', {
      'fields': ('user', 'due_date',)
    }),
  )


class CarModelAdmin(admin.ModelAdmin):
  list_display = ('make', 'model')

class CarAdmin(admin.ModelAdmin):
  list_display = ('model_id', 'plate', 'vin', 'owner', 'cover')
  search_fields = ('vin', 'model_id__make')  
  list_filter = ('owner', 'model_id__make')
  inlines = [OrderInline]
  

class ServiceAdmin(admin.ModelAdmin):
  list_display = ('service', 'price')

admin.site.register(CarModel, CarModelAdmin)
admin.site.register(Car, CarAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderRow, OrderRowAdmin)
admin.site.register(Service, ServiceAdmin)