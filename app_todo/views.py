from django.shortcuts import render
import requests
from app_todo.models import Task_Todo
from app_todo.forms import TodoForm
from django.http import JsonResponse
from .serializers import TaskTodoSerializer
from rest_framework import mixins
from rest_framework.permissions import  IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.generics import ListCreateAPIView


@api_view(['GET'])
def apiOverview(request):
  api_urls ={
    'List':'/api-tasktodo-list/',
    'Detail View':'/api-tasktodo-detail/<str:pk>',
    'Create':'/api-tasktodo-create',
    'Update':'/api-tasktodo-update/<str:pk>',
    'Delete':'/api-tasktodo-delete/<str:pk>',
  }
  return Response(api_urls)


# sample code - to minimal  these are same 'todo_PostView,todo_CreateView'
class todo_PostView(
  mixins.ListModelMixin ,  
  mixins.CreateModelMixin,
  generics.GenericAPIView):

  serializer_class = TaskTodoSerializer
  queryset= Task_Todo.objects.all()

  def get(self,request, *args,**kwargs):
    return self.list(request, *args,**kwargs)
    
  def post(self,request, *args,**kwargs):
    return self.create(request, *args,**kwargs)



class todo_CreateView (mixins.ListModelMixin , generics.CreateAPIView):
  serializer_class= TaskTodoSerializer
  queryset = Task_Todo.objects.all()

  def get(self,request, *args,**kwargs):
    return self.list(request, *args,**kwargs)



class todo_listCreateView (ListCreateAPIView):
  serializer_class= TaskTodoSerializer
  queryset = Task_Todo.objects.all()


    
# class TestView(APIView):
#   permission_classes=(IsAuthenticated,)

#   def get(self,request, *args,**kwargs):
#     qs = Task_Todo.objects.all()
#     serializer = TaskTodoSerializer(qs, many =True)
#     return Response(serializer.data)
  

#   def post(self,request, *args,**kwargs):
#     serializer= TaskTodoSerializer(data=request.data)
#     if serializer.is_valid():
#       serializer.save()

#       return Response(serializer.data)
#     return Response(serializer.errors)

  

def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'


def todo_Dashboard(request):
  todo_data = Task_Todo.objects.filter(user=request.user).order_by
  ('user','created_at',)

  todo_data= requests.get('http://127.0.0.1:8000/app_todo/api-todoPostView/').json()

  


  print(f'todo data : --->>> {todo_data}')
  form = TodoForm()

  template ='app_todo/todo-dashboard.html'
  context={'todo_data':todo_data,'form':form}
  return render(request,template, context)



def data_list_Todo():
  mrec=Task_Todo.objects.all().values('title','completed')
  mlist = list(mrec)
  return mlist

def TodoAddRecord_bak(request):

  if is_ajax(request):
    form = TodoForm(request.POST)
    if form.is_valid():
      print(f'form is valid')
      data = form.save(commit=False)
      data.user = request.user
      data.save()
      datalist=data_list_Todo()
      response = {'status':'success','message':f'{data.title} has been saved','datalist':datalist}
      return JsonResponse(response)
    else:
      print(f'form is invalid')
      response = {'status':'failed','message':'invalid form'}
      return JsonResponse(response)
  else  :
    response = {'status':'failed','message':'it is not an ajax request'}
    return JsonResponse(response)
  
def TodoAddRecord(request):

  if is_ajax(request):
    form = TodoForm(request.POST)

    if form.is_valid():
      print(f'form is valid')
      data = form.save(commit=False)
      data.user = request.user
      data.save()
      datalist=data_list_Todo()
      response = {'status':'success','message':f'{data.title} has been saved','datalist':datalist}
      return JsonResponse(response)
    else:
      print(f'form is invalid')
      response = {'status':'failed','message':'invalid form'}
      return JsonResponse(response)
  else  :
    response = {'status':'failed','message':'it is not an ajax request'}
    return JsonResponse(response)



# calling serializer


@api_view(['GET'])
def Task_Todo_List(request):
  task_todo = Task_Todo.objects.all()
  serializer = TaskTodoSerializer(task_todo, many=True)
  return Response(serializer.data)

@api_view(['GET'])
def Task_Todo_Detail(request,pk):
  task_todo = Task_Todo.objects.get(id=pk)
  serializer = TaskTodoSerializer(task_todo, many=False)
  return Response(serializer.data)

@api_view(['POST'])
def Task_Todo_Create(request):
  
  serializer = TaskTodoSerializer( data= request.data)
  if serializer.is_valid():
    print(f'serializer is valid ')
    serializer.save(user=request.user)
  return Response(serializer.data)

@api_view(['POST'])
def Task_Todo_Update(request,pk):
  task_todo = Task_Todo.objects.get(id=pk)
  serializer = TaskTodoSerializer( instance=task_todo , data= request.data)

  if serializer.is_valid():
      serializer.save()
  return Response(serializer.data)

@api_view(['DELETE'])
def Task_Todo_Delete(request,pk):
  task_todo = Task_Todo.objects.get(id=pk)
  task_todo.delete()
  return Response("item deleted")



