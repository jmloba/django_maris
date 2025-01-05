

from django.urls import  include, re_path, path
from .views import StudentsViewSet, ModulesViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("student", StudentsViewSet, basename='student')

router.register("module", ModulesViewSet, basename='module')

app_name ='app_manytomany_api'

urlpatterns=[
  path('', include(router.urls))

]
