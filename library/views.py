from django.shortcuts import render
from django.http import HttpResponse
from .models import Book, Author, BookInstance, Genre
from django.shortcuts import render, get_object_or_404
from django.views import generic

def index(request):
    
    # Suskaičiuokime keletą pagrindinių objektų
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    
    # Laisvos knygos (tos, kurios turi statusą 'g')
    num_instances_available = BookInstance.objects.filter(status__exact='g').count()
    
    # Kiek yra autorių    
    num_authors = Author.objects.count()
    
    # perduodame informaciją į šabloną žodyno pavidale:
    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
    }

    # renderiname index.html, su duomenimis kintamąjame context
    return render(request, 'library/index.html', context=context)

def authors(request):
    
    authors = Author.objects.all()
    context = {
        'authors': authors
    }
    print(authors)
    return render(request, 'library/authors.html', context=context)

def author(request, author_id):
    single_author = get_object_or_404(Author, pk=author_id)
    return render(request, 'library/author.html', {'author': single_author})

class BookListView(generic.ListView):
    model = Book
    template_name = 'library/book_list.html'

class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'library/book_detail.html'

# def book_detail(request, slug):
#     unique_slug = get_object_or_404(Book, slug = slug)
#     return render(request, "book_detail.html", {"book": unique_slug})