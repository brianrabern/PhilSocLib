from django.shortcuts import render
from libraryapp.models import Book
from django.db.models import Q


def book_list(request):
    books = Book.objects.all()
    context ={"books": books}

    return render(request,"library/books.html",context)


def search(request):
    if request.method == "POST":
        searched = request.POST.get("searched")
        books = Book.objects.filter(Q(title__contains=searched) | Q(author__contains=searched)|Q(call_number__contains=searched))
        context = {'searched': searched, 'books': books}
        return render(request,'library/search.html', context)
    else:
        return render(request,'library/search.html', {})
