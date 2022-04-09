from django.urls import path, include

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
    path('i18n/', include('django.conf.urls.i18n')),
    path('userorders/', views.UserOrders.as_view(), name='user-orders'),
    path('userorders/<int:pk>', views.UserOrdersDetail.as_view(), name='user-order'),
    path('userorders/new', views.UserOrderCreateView.as_view(), name='user-orders-new'),
    path('userorders/<int:pk>/update', views.UserOrderUpdateView.as_view(), name='user-order-update'),
    path('userorders/<int:pk>/delete', views.UserOrderDeleteView.as_view(), name='user-order-delete'),
    path('userorders/<int:pk>/newrow', views.OrderRowCreateView.as_view(), name='row-new'),
]