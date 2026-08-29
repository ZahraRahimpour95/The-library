from django.shortcuts import render,redirect, get_object_or_404
from book.models import *
from .forms import BookForm 

def book_list (request):

    query = request.GET.get('q')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    publication_date = request.GET.get('publication_date')

    books = Books.objects.all()

    #search
    if query:
        books = Books.objects.filter(title__icontains = query
                                     )| Books.objects.filter(
                                         author__first_name__icontains = query
                                     )| Books.objects.filter(
                                         author__last_name__icontains = query
                                     )
        

    is_filtered = False

    #price filter
    if min_price :
        books = Books.objects.filter(price__gte = min_price)
        is_filtered = True

    if max_price:
        books = Books.objects.filter(price__lte = max_price)
        is_filtered = True

    #publication_date filter 
    if publication_date :
        books = Books.objects.filter(publication_date__gte = publication_date)
        is_filtered = True

    # Delete filtered books
    if request.method == 'POST' and is_filtered :

        min_price = request.POST.get('min_price')
        max_price = request.POST.get('max_price')
        publication_date = request.POST.get('publication_date')

        books = Books.objects.all()

        if min_price:
            books = books.filter(price__gte=min_price)

        if max_price:
            books = books.filter(price__lte=max_price)

        if publication_date:
            books = books.filter(publication_date__gte=publication_date)

        books.delete()

        return redirect('book_list')
        

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

def delete_book(request, book_id):
    book = get_object_or_404(Books , id = book_id)

    book.delete()
    return redirect('book_list')