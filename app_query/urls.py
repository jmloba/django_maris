from django.contrib import admin
from django.urls import include, re_path,path
from app_query import views
from .views import UpdateDeleteTeacher_ajax, updateDelete_modal2




app_name ='app_query'
urlpatterns = [
  path('query-dashboard/',views.query_Dashboard, name='query-dashboard'),

  path('create-record-modal-qtest/',views.create_record_modal_qtest, name='create-record-modal-qtest'),   
  
  path('query-tasktable/',views.query_tasktable, 
  name='query-tasktable'),
  path('query-classroom/',views.query_classroom, name='query-classroom'),

  path('add-record-teacher/',views.add_record_teacher, name='add-record-teacher'),
  path('add-edit-record-teacher-ajax/',views.add_edit_record_teacher_ajax, name='add-edit-record-teacher-ajax'),

  path('UpdateDeleteTeacher-ajax/<int:pk>/',UpdateDeleteTeacher_ajax.as_view(), name='UpdateDeleteTeacher-ajax'),


  path('queryTableModal/',views.queryTableModal, 
  name='queryTableModal'),

  path('TaskAddEditRecord/',views.TaskAddEditRecord, 
  name='TaskAddEditRecord'),

  # path('Task-Update-Delete/<int:pk>',views.Task_Update_Delete, 
  # name='Task-Update-Delete'),
  path('UpdateDelete-modal/',views.TaskAddEditRecord, 
  name='UpdateDelete-modal'),

  path('updateDelete-modal2/<int:pk>/',updateDelete_modal2.as_view(), 
  name='updateDelete-modal2'),
  
  
]
