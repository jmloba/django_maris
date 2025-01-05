from django.contrib import admin
from django.urls import include, re_path,path
from app_manytomany import views
# from .views import UpdateDeleteTeacher_ajax, updateDelete_modal2,queryall_updatedelete_task 




app_name ='app_manytomany'
urlpatterns = [

  path('StudentDashboard/',views.StudentDashboard, 
  name='StudentDashboard'),  

  path('StudentAddNewRecord/',views.StudentAddNewRecord, 
  name='StudentAddNewRecord'),  
  
path('view-relate/<int:pk>',views.view_relate, 
  name='view-relate'),  
  
]