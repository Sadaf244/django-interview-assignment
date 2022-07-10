from django.urls import path
from .views import *
urlpatterns = [
    path('',SignupView.as_view(),name='signup'),
    #https://my-application-library.herokuapp.com
    path('login/',CustomAuthToken.as_view(),name='login'),
    #https://my-application-library.herokuapp.com/login/
    path('getupdatedeletemember/',MemberView),
    #https://my-application-library.herokuapp.com/getupdatedeletemember/
    path('deleteaccount/',DeleteAccountView),
    #https://my-application-library.herokuapp.com/deleteaccount/
]