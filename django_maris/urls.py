
from django.contrib import admin
from django.urls import path

from django.contrib import admin

from django.urls import include,  path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

from . import views

from debug_toolbar.toolbar import debug_toolbar_urls


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.home , name ='home' ),     

    path('app_task/'        , include('app_task.urls')),
    path('app_accounts/'    , include('app_accounts.urls')),
    path('app_query/'       , include('app_query.urls')),
    path('app_manytomany/'  , include('app_manytomany.urls')),    
    path('app_todo/'        , include('app_todo.urls')),    
    path('__debug__/'   , include('debug_toolbar.urls')),
    path('api/'        , include('api.urls')),    


  path('dj-rest-auth/', include('dj_rest_auth.urls')),
  path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls'))
]
if settings.DEBUG:
    # urlpatterns+=  debug_toolbar_urls()
    urlpatterns+= staticfiles_urlpatterns()
    urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    