from django.urls import path
from libraryapp.views import book_list, search, book_detail, checkout
from libraryapp.views import home_view, contact, confirm

urlpatterns = [
    path('home/', home_view, name="home"),
    path('contact/', contact, name="contact"),
    path('list/', book_list, name="list"),
    path('search/', search, name="search"),
    path('details/<int:id>/', book_detail, name="details"),
    path('checkout/<int:id>/', checkout, name="checkout"),
    path('confirm/<int:id>/', confirm, name="confirm"),
]
