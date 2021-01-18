
from django.contrib import admin
from django.urls import path,re_path,include
from . import views

app_name ="Users"
urlpatterns = [
    path('login', views.LoginUsuer.as_view(),name="login"),
    path('register', views.registerView.as_view(),name="register"),
    path('logout', views.Logout.as_view(),name="logout"),
    #incluyo las url propias
]
