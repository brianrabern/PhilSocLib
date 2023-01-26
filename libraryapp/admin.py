from django.contrib import admin
from libraryapp.models import Book,Borrow

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display =("call_number", "title", "author")

@admin.register(Borrow)
class BorrowAdmin(admin.ModelAdmin):
        list_display =("borrower_name", "book","checked_out")
