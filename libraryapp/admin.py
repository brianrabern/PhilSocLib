from django.contrib import admin
from libraryapp.models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display =("call_number", "title", "author")
