from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='servisiux/index'),
    path('stats/', views.stats, name='stats'),
    path('cars/', views.cars, name='cars'),
    path('cars/<int:car_id>', views.car, name='car'),
    path('orders/', views.OrderListView.as_view(), name='orders'),
    path('orders/<int:pk>/', views.OrderDetailView.as_view(), name='order-detail'),
    path('search/', views.search, name='servisiux/search'),
    path('myorders/', views.UserOrdersListView.as_view(), name='my-orders'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='servisiux/profile'),
]