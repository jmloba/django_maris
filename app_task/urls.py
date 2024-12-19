from django.contrib import admin
from django.urls import include, re_path,path
from app_task import views

app_name ='app_task'
urlpatterns = [
  path('task-dashboard/',views.task_Dashboard, name='task-dashboard'),
  
  path('create-record-modal/',views.create_record_modal, name='create-record-modal'),     
  path('Task-delete-record/<int:pk>',views.TaskDeleteRecord, name='Task-delete-record'),    

  path('Task-update-record/<int:pk>',views.update_record, name='Task-update-record'), 
  
  path('post-entries/',views.post_entries, name='post-entries'),

  path('view-item/<int:pk>/',views.view_item, name='view-item'),  

  path('history-view/<int:pk>/',views.history_view, name='history-view'),    

  path('create-history-record-modal/',views.create_history_record_modal, name='create-history-record-modal'), 

  path('ajax/load-MFOsub/', views.ajax_load_MFOsub, name='ajax_load_MFOsub'),
  path('ajax/load-MFOsub2/', views.ajax_load_MFOsub2, name='ajax_load_MFOsub2'),
     
     
path('history-delete-record/<int:pk>,<int:reference>',views.history_delete_record, 
name='history-delete-record'),   

path('history-update-record/<int:pk>,<str:ref>',views.history_update_record, 
name='history-update-record'),     

path('dashboard-mfo/',views.dashboard_mfo, name='dashboard-mfo'),    
path('dashboard-mfosub/',views.dashboard_mfosub, name='dashboard-mfosub'),    

path('dashboard-mfosub2/',views.dashboard_mfosub2, name='dashboard-mfosub2'),    

path('mfo-delete-record/<int:pk>',views.mfo_delete_record, 
name='mfo-delete-record'),    

path('mfosub2-delete-record/<int:pk>',views.mfosub2_delete_record, 
name='mfosub2-delete-record'),  

path('mfosub-delete-record/<int:pk>',views.mfosub_delete_record, 
name='mfosub-delete-record'),    


path('print-task-ajax/',views.print_task_ajax, 
name='print-task-ajax'),    

   
]