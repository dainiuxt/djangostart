from operator import mod
from django.db import models
from django.urls import reverse

# Create your models here.

'''
Sukurti visus modelius pagal nurodytą programos DB struktūrą
Sukurti meniu punktus visiems sukurtiems modeliams
'''

class CarModel(models.Model):
  make = models.CharField('Make', max_length=200)
  model = models.CharField('Model', max_length=200)

  def __str__(self):
      return (f"{self.make}, {self.model}")

  class Meta:
      verbose_name = 'Model'
      verbose_name_plural = 'Models'        


class Car(models.Model):
  plate = models.CharField('License plate', max_length=200)
  model_id = models.ForeignKey('Carmodel', on_delete=models.SET_NULL, null=True)
  vin = models.CharField('VIN number', max_length=200)
  owner = models.CharField('Owner name, surname', max_length=200)

  def __str__(self):
      return self.plate  

  class Meta:
      verbose_name = 'Car'
      verbose_name_plural = 'Cars'


class Order(models.Model):
  date = models.CharField('Date', max_length=200)
  car_instance_id = models.ForeignKey('Car', on_delete=models.SET_NULL, null=True)

  def __str__(self):
      return self.car_instance_id

  class Meta:
      verbose_name = 'Order'
      verbose_name_plural = 'Orders'


class OrderRow(models.Model):
  service_id = models.ForeignKey('Service', on_delete=models.SET_NULL, null=True)
  order_id = models.ForeignKey('Order', on_delete=models.SET_NULL, null=True)
  quantity = models.IntegerField('Quantity')
  # price = models.ManyToManyField('Service', max_length=200)

  def __str__(self):
      return self.order_id

  class Meta:
      verbose_name = 'Row'
      verbose_name_plural = 'Rows'  


class Service(models.Model):
  service = models.CharField('Service', max_length=200)
  price = models.FloatField('Price', max_length=200)

  def __str__(self):
      return self.service

  class Meta:
      verbose_name = 'Service'
      verbose_name_plural = 'Services'      