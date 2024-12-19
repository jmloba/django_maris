
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponse
from django.utils.timezone import localdate
from django.db.models import Sum,Count
from app_task.models import TaskTable

# @login_required(login_url='app_accounts:login-view')
def home(request):
  totalrecords=len(TaskTable.objects.all())
  

  print(f'total records:  {totalrecords}')

  
  context = {'totalrecords':totalrecords  }
  return render(request,'home.html',context )