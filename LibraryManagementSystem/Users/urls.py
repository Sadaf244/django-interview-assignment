from django.urls import path
from .views import *
urlpatterns = [
    path('signup/',SignupView.as_view(),name='signup'),
    #http://localhost:8000/signup/
    path('login/',CustomAuthToken.as_view(),name='login'),
    #http://localhost:8000/login/
    path('getupdatedeletemember/',MemberView),
    #http://localhost:8000/getupdatedeletemember/
    path('deleteaccount/',DeleteAccountView),
    #http://localhost:8000/deleteaccount/
]