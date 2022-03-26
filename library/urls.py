from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='library/index'),
    path('authors/', views.authors, name='authors'),
    path('authors/<int:author_id>/', views.author, name='author'),
    path('books/', views.BookListView.as_view(), name='books'),
    # path('books/<slug:slug>/', views.book_detail, name='book-detail'),
    path('books/<int:pk>/', views.BookDetailView.as_view(), name='book-detail'),
]