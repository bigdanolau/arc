
from django.contrib import admin
from django.urls import path,re_path,include
from . import views
urlpatterns = [
    path('tareas/home', views.TareasListView.as_view()),
    path('tareas/update', views.TareasListView.as_view()),
    path('tareas/crear', views.CrearTarea.as_view()),
    path('tareas/detalle/<pk>/<deuda>', views.detalleTarea.as_view()),
    path('tareas/listado/<pk>', views.listadoTarea.as_view()),
    #incluyo las url propias
]
