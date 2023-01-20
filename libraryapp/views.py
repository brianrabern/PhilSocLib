from django.shortcuts import render

from libraryapp.models import Book


def book_list(request):
    books = Book.objects.all()
    context ={"books": books}

    return render(request,"library/books.html",context)
