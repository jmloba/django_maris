
from django.contrib import admin
from django.urls import path

from django.contrib import admin

from django.urls import include,  path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

from . import views




urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.home , name ='home' ),     

    path('app_task/', include('app_task.urls')),
    path('app_accounts/', include('app_accounts.urls')),
]
if settings.DEBUG:
    urlpatterns+= staticfiles_urlpatterns()
    urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
