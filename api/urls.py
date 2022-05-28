from django.urls import path
from api.views import getBook, getBooks

urlpatterns = [

    path('', getBooks, name="books"),
    path('<str:pk>/', getBook, name="book"),
   
]