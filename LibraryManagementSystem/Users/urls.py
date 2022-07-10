from django.urls import path
from .views import *
urlpatterns = [
    path('signup/',SignupView.as_view(),name='signup'),
    #https://my-application-library.herokuapp.com/users/signup/
    path('login/',CustomAuthToken.as_view(),name='login'),
    #https://my-application-library.herokuapp.com/users/login/
    path('getupdatedeletemember/',MemberView),
    #https://my-application-library.herokuapp.com/users/getupdatedeletemember/
    path('deleteaccount/',DeleteAccountView),
    #https://my-application-library.herokuapp.com/users/deleteaccount/
]