from django.urls import path
from .views import *
urlpatterns = [
    path('GetUpdateDeleteBook/',BookView),
    #https://my-application-library.herokuapp.com/book/GetUpdateDeleteBook/?id=3
    path('BookCreate/',BookCreateView.as_view(), name='BookCreateView'),
    #https://my-application-library.herokuapp.com/book/BookCreate/
    path('readbook/',ReadView),
    #https://my-application-library.herokuapp.com/book/readbook/
    path('returnbook/',ReadDeleteView),
    #https://my-application-library.herokuapp.com/book/returnbook/?id=1
    path('viewbook/',BookListView.as_view(), name='BookView'),
    #https://my-application-library.herokuapp.com/book/viewbook/
   
]