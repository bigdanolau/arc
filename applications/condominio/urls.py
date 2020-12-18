
from django.contrib import admin
from django.urls import path,re_path,include
from . import views

app_name ="condominio"
urlpatterns = [
    path('home', views.CondominioListView.as_view(),name="condominioHome"),
    path('importar', views.ImportarExcel.as_view())
    #incluyo las url propias
]
