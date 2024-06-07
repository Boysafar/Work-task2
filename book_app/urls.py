from django.urls import path
from . import views

urlpatterns = [
    # Other URL patterns...
    path('', views.books_list, name='books_list'),
]
