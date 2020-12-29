
from django.contrib import admin
from django.urls import path,re_path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('',include('applications.condominio.urls')),
    re_path('',include('applications.seguimiento.urls')),
    re_path('',include('applications.users.urls'))
    #incluyo las url propias
]
