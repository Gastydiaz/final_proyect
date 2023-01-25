from django.contrib import admin
from django.urls import path, include
from movies.views import index
from entregable_final.settings import MEDIA_ROOT, MEDIA_URL
from django.conf.urls.static import static


urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('movies/', include('movies.urls')),
    path('users/', include('users.urls')),
    
] + static(MEDIA_URL, document_root= MEDIA_ROOT)
