
from django.contrib import admin
from django.urls import path,re_path,include
from . import views
urlpatterns = [
    path('home', views.CondominioListView.as_view()),
    path('importar', views.ImportarExcel.as_view())
    #incluyo las url propias
]
