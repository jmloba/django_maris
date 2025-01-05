from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from rest_framework.response import Response
from rest_framework import status, generics

from app_todo.models import Task_Todo
from api.serializers import TaskTodoSerializer  ## with fields all

# using function view

@api_view(['GET'])
def get_TaskTodo(request):
  data = Task_Todo.objects.all()
  serializer=TaskTodoSerializer(data, many=True)
  return Response(serializer.data)

@api_view(['POST'])
def apiTaskTodoAddRecord(request):
  # get the data from frontend
  serializer =TaskTodoSerializer(data=request.data)
  if serializer.is_valid():
    serializer.save()
    
    response =(serializer.data)
    return Response(response)
  # return error
  return Response(serializer.errors)


@api_view(['GET','PUT', 'DELETE'])
def apiTaskTodoDetail(request,pk):
  try:
    data = Task_Todo.objects.get(pk=pk)
  except Task_Todo.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)  
  
  if request.method =='GET':
    serializer = TaskTodoSerializer(data)
    return Response(serializer.data)
  elif request.method =='PUT':  # edit or update
    serializer = TaskTodoSerializer(data,data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
  elif   request.method =='DELETE':
    data.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)  


#using class view  --------

class apiCLassTaskTodoCreate(generics.ListCreateAPIView):
  queryset = Task_Todo.objects.all()
  serializer_class=TaskTodoSerializer

  def delete(self, request, *args,**kwargs):
    Task_Todo.objects.all().delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


class apiCLassTaskTodoRetriveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
  queryset = Task_Todo.objects.all()
  serializer_class=TaskTodoSerializer
  lookup_field ='pk'


# creating queries
class apiclassTodoList(APIView):
  def get(self, request,format = None):
    title = request.query_params.get("title",'')

    if title:
      # filter queryset based on given title
      todos = Task_Todo.objects.filter(title__icontains=title)
    else:
      # if no title provided return all
      todos = Task_Todo.objects.all()

    serializer = TaskTodoSerializer(todos, many=True)  
    
    return Response(serializer.data, status=status.HTTP_200_OK)



