
from django.contrib import admin
from django.urls import path,re_path,include
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('',include('applications.condominio.urls')),
    re_path('',include('applications.seguimiento.urls')),
    re_path('',include('applications.users.urls')),
    re_path('',include('applications.comentarios.urls'))
    #incluyo las url propias
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
