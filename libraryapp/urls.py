from django.urls import path
from libraryapp.views import book_list

urlpatterns = [
    path('', book_list, name ="list")
]
