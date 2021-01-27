
from django.contrib import admin
from django.urls import path,re_path,include
from . import views

app_name ="comentario"
urlpatterns = [
    path('comentario/add', views.ComentarioCreateView.as_view())
    #incluyo las url propias
]
