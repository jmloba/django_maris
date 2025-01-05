from django.contrib import admin
from django.urls import include, re_path,path
from app_query import views
from app_todo import views

from app_todo.views import todo_PostView, todo_CreateView, todo_listCreateView


from rest_framework.authtoken.views import obtain_auth_token




app_name ='app_todo'
urlpatterns = [
  path('',views.apiOverview, name='api-overview'),

  path('todo_dashboard/',views.todo_Dashboard, name='todo_dashboard'),

  path('TodoAddRecord/',views.TodoAddRecord, name='TodoAddRecord'),  
  
  
  # for serializers
  path('api-tasktodo-list/',views.Task_Todo_List, name='api-tasktodo-list'),  

  path('api-tasktodo-detail/<str:pk>/',views.Task_Todo_Detail, name='api-tasktodo-detail'),  

  path('api-tasktodo-create/',views.Task_Todo_Create, name='api-tasktodo-create'),  

  path('api-tasktodo-update/<str:pk>/',views.Task_Todo_Update, name='api-tasktodo-update'),  

  path('api-tasktodo-delete/<str:pk>/',views.Task_Todo_Delete, name='api-tasktodo-delete'),  


# sample --------

  path('api-todoPostView/',todo_PostView.as_view(), name='api-todoPostView'),  



  path('api-todoCreateView/', todo_CreateView.as_view(), name='api-todoCreateView'),  



  path('api-todo-listCreateView/',todo_listCreateView.as_view(), name='api-todo-listCreateView'),  

# sample --------


  path('api-token/',obtain_auth_token, name='obtain-token'),  
  
  

]
