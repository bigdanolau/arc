
from django.contrib import admin
from django.urls import path,re_path,include
from . import views
urlpatterns = [
    path('tareas/home', views.TareasListView.as_view())
    #incluyo las url propias
]
