from django.urls import path
from .views import get_books, create_order

urlpatterns = [
    path('books/', get_books),
    path('orders/', create_order),
]
