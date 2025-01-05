
from django.contrib import admin
from django.urls import include, re_path,path
from api import views
from api.views import apiCLassTaskTodoCreate,apiCLassTaskTodoRetriveUpdateDestroy, apiclassTodoList

app_name ='api'
urlpatterns = [
# function view  
path('api-TaskTodo/',views.get_TaskTodo, name='api-TaskTodo'),  
path('api-TaskTodo/AddRec/',views.apiTaskTodoAddRecord, name='api-TaskTodoAddRec'),  
path('api-TaskTodoDetail/<int:pk>',views.apiTaskTodoDetail, name='api-apiTaskTodoDetail'),  

# class view

# added delete all inside this
path('apiclass-TaskTodoCreate/',apiCLassTaskTodoCreate.as_view(), name='apiclass-TaskTodoCreate'),  

path('apiclass-TaskTodo-RUD/<int:pk>',apiCLassTaskTodoRetriveUpdateDestroy.as_view(), name='apiclass-TaskTodo-RUD'),  

path('apiclass-TaskTodo-list/',apiclassTodoList.as_view(), name='apiclass-TaskTodo-list'),  



]