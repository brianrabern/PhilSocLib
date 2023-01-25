from django.urls import path
from libraryapp.views import book_list, search, book_detail,checkout, home_view, contact

urlpatterns = [
    path('home/', home_view, name ="home"),
    path('contact/', contact, name ="contact"),
    path('list/',book_list, name="list"),
    path('search/', search, name ="search"),
    path('details/<int:id>/', book_detail, name ="details"),
    path('checkout/<int:id>/', checkout, name ="checkout")
]
