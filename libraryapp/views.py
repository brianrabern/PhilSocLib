from django.shortcuts import render, get_object_or_404,redirect
from libraryapp.models import Book, Borrow
from django.db.models import Q
from libraryapp.forms import BorrowForm



def confirm(request,id):
    borrow = Borrow.objects.get(id=id)

    # borrow = get_object_or_404(Borrow)
    context = {"borrow": borrow}
    return render(request, "library/confirm.html", context)


def checkout(request,id):
    book = get_object_or_404(Book, id=id)
    if request.method == "POST":
        form = BorrowForm(request.POST,initial={"book": book})
        if form.is_valid():
            book.available -= 1
            book.save()
            borrow = form.save(False)
            borrow.save()
            return redirect('confirm',borrow.id)
    else:
        form=BorrowForm(initial={"book": book})
        #
    context = {"form": form, "book": book}
    return render(request, "library/checkout.html", context)

def contact(request):
    return render(request,"library/contact.html")

def home_view(request):
    books = Book.objects.all()
    context ={"books": books}
    return render(request,"library/home.html", context)

def book_list(request):
    books = Book.objects.all()
    context ={"books": books}

    return render(request,"library/books.html",context)


def search(request):
    if request.method == "POST":
        searched = request.POST.get("searched")
        books = Book.objects.filter(Q(title__contains=searched) | Q(author__contains=searched)|Q(call_number__contains=searched)|Q(year__contains=searched))
        context = {'searched': searched, 'books': books}
        return render(request,'library/search.html', context)




def book_detail(request,id):
    book = get_object_or_404(Book,id=id)
    context ={
        "book": book
    }
    return render(request, "library/detail.html", context)
