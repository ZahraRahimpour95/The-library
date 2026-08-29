from django.shortcuts import render,redirect, get_object_or_404
from book.models import *
from .forms import BookForm 

def book_list (request):
    query = request.GET.get('q')
    if query:
        books = Books.objects.filter(title__icontains = query
                                     )| Books.objects.filter(
                                         author__first_name__icontains = query
                                     )| Books.objects.filter(
                                         author__last_name__icontains = query
                                     )
    else:
        books = Books.objects.all()

    return render (
        request, 
        'book/book_list.html',
        {'books' : books}
    )

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('book_list')

    else:
        form = BookForm()

    return render(
        request,
        'book/add_book.html',
        {'form': form}
    )

def edit_book(request, book_id):

    book = get_object_or_404(Books, id=book_id)

    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)

        if form.is_valid():
            form.save()
            return redirect('book_list')

    else:
        form = BookForm(instance=book)

    return render(
        request,
        'book/edit_book.html',
        {'form': form}
    )