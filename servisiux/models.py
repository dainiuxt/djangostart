from django.db import models

# Create your models here.

class CarModel(models.Model):
  make = models.CharField('Make', max_length=200)
  model = models.CharField('Model', max_length=200)

  def __str__(self):
      return (f"{self.make} {self.model}")

  class Meta:
      verbose_name = 'Model'
      verbose_name_plural = 'Models'        


class Car(models.Model):
  plate = models.CharField('License plate', max_length=200)
  model_id = models.ForeignKey('Carmodel', on_delete=models.SET_NULL, null=True, related_name="carmodel")
  vin = models.CharField('VIN number', max_length=200)
  owner = models.CharField('Owner name, surname', max_length=200)
  cover = models.ImageField('Carpic', upload_to='service/cars', null=True)

  @property
  def car_suma(self):
      orders = Order.objects.filter(car_instance_id=self.id)
      recipe = 0
      for row in orders:
          recipe += row.suma
      return recipe

  def __str__(self):
      return f'{self.plate}'

  class Meta:
      verbose_name = 'Car'
      verbose_name_plural = 'Cars'


class Order(models.Model):
  date = models.DateField('Date', null=True, blank=True)
  car_instance_id = models.ForeignKey('Car', on_delete=models.SET_NULL, null=True, related_name='carorder')
#   link = models.CharField('link', max_length=50, default='Open order')

  @property
  def suma(self):
      order_rows = OrderRow.objects.filter(order_id=self.id)
      recipe = 0
      for row in order_rows:
          recipe += row.quantity * row.service_id.price
      return recipe

  def __str__(self):
      return f'{self.car_instance_id}'

  class Meta:
      verbose_name = 'Order'
      verbose_name_plural = 'Orders'
  
  def save(self, *args, **kwargs):
      self.link = f'Open order'
      super().save(*args, **kwargs)

  ORDER_STATUS = (
    ('e', 'Entered'),
    ('w', 'Waiting'),
    ('p', 'In progress'),
    ('c', 'Completed'),
    )

  status = models.CharField(
    max_length=1,
    choices=ORDER_STATUS,
    blank=True,
    default='e',
    help_text='Status',
    )


class OrderRow(models.Model):
  service_id = models.ForeignKey('Service', on_delete=models.SET_NULL, null=True)
  order = models.ForeignKey('Order', on_delete=models.SET_NULL, null=True)
  quantity = models.IntegerField('Quantity')
  # price = models.ManyToManyField('Service', max_length=200)

  def __str__(self):
      return f'{self.order_id}, {self.quantity}'

  # def service_data(service_id):
  #     return Service.objects.get(service_id)

  class Meta:
      verbose_name = 'Row'
      verbose_name_plural = 'Rows'  
      unique_together = ('service_id', 'order')


class Service(models.Model):
  service = models.CharField('Service', max_length=200)
  price = models.FloatField('Price', max_length=200)

  def __str__(self):
      return f'{self.service}'

  class Meta:
      verbose_name = 'Service'
      verbose_name_plural = 'Services'      