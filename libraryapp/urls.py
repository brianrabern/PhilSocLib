from django.urls import path
from libraryapp.views import book_list, search

urlpatterns = [
    path('', book_list, name ="list"),
    path('search/', search, name ="search")
]
