from django.contrib import admin
from django.urls import include, re_path,path
from app_task import views

app_name ='app_task'
urlpatterns = [
  path('task-dashboard/',views.task_Dashboard, name='task-dashboard'),
  
  path('create-record-modal/',views.create_record_modal, name='create-record-modal'),     
  path('Tasl-delete-record/<int:pk>',views.TaskDeleteRecord, name='Task-delete-record'),    
  path('Task-update-record/<int:pk>',views.update_record, name='Task-update-record'), 
  path('post-entries/',views.post_entries, name='post-entries'),

  path('view-item/<int:pk>/',views.view_item, name='view-item'),  

]