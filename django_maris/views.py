
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponse
from django.utils.timezone import localdate
from django.db.models import Sum,Count
from app_task.models import TaskTable

from rest_framework.decorators import api_view
from rest_framework.response import Response


# @login_required(login_url='app_accounts:login-view')
def home(request):
  totalrecords=len(TaskTable.objects.all())
  

  print(f'total records:  {totalrecords}')

  
  context = {'totalrecords':totalrecords  }
  return render(request,'home.html',context )

@api_view(['POST'])
def login(request):
  print(f'test login ***')
  response= {}
  return Response(response)


@api_view(['POST'])
def signup(request):
  print(f'test signp ***')
  response= {}
  return Response(response)

@api_view(['POST'])
def test_token(request):
  print(f'test token')
  response= {}
  return Response(response)


