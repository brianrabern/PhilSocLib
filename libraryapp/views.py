from django.shortcuts import render, get_object_or_404,redirect
from libraryapp.models import Book
from django.db.models import Q
from libraryapp.forms import BorrowForm


def checkout(request,id):
    book = get_object_or_404(Book, id=id)
    if request.method == "POST":
        form = BorrowForm(request.POST,initial={"book": book})
        if form.is_valid():
            borrow = form.save(False)
            borrow.save()
            return redirect('list')
    else:
        form=BorrowForm(initial={"book": book})
        #
    context = {"form": form, "book": book}
    return render(request, "library/checkout.html", context)



def contact(request):
    return render(request,"library/contact.html")

def home_view(request):
    return render(request,"library/home.html")

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


def book_detail(request,id):
    book = get_object_or_404(Book,id=id)
    context ={
        "book": book
    }
    return render(request, "library/detail.html", context)
