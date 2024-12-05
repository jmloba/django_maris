from django.shortcuts import get_object_or_404, render,redirect
from .models import TaskTable,FileSerials

from django.db.models import ExpressionWrapper, F, fields, Func
from app_accounts.models import UserAccess
from .forms import TaskTableForm,DeleteRecordTaskForm,UpdateRecordTaskForm

from django.utils.timezone import timedelta
import datetime
from django.contrib import messages
from app_task.utils import generate_posting_refno
from datetime import datetime


# Create your views here.


def task_Dashboard(request):
  

  user_access = UserAccess.objects.get(user=request.user)
  form = TaskTableForm()

  if user_access.supervisor:
    data = TaskTable.objects.all()
    
  else:  
    data = TaskTable.objects.filter(user=request.user)

  context={'data':data, "form":form,'user_access':user_access}
  return render(request,'app_task/task_Dashboard.html', context)

def create_record_modal(request):
  if request.method== 'POST':
    form = TaskTableForm(request.POST or None, request.FILES or None)
        
    if form.is_valid():
      print('form is valid')
      post = form.save(commit=False)
      post.diff=form.cleaned_data['date_to']-form.cleaned_data['date_from']

      post.user=request.user
      post.save()      

      data=TaskTable.objects.all()
      context={'data':data, 'form':form }

      return redirect('app_task:task-dashboard', )
    
def TaskDeleteRecord(request,pk=None):

  data= TaskTable.objects.get(id=pk)
  form = DeleteRecordTaskForm(instance = data) 
  if request.method=='POST':
    data.delete()   
    return redirect('app_task:task-dashboard', )
  

  context={'form':form,'datarec':data}
  return render(request,'app_task/delete_task.html', context)


def update_record(request, pk=None):
  data= TaskTable.objects.get(id=pk)
  form = UpdateRecordTaskForm(instance =data)
  if request.method=='POST':

    form = UpdateRecordTaskForm(request.POST or None, instance = data)
    if form.is_valid():  
      post = form.save(commit=False)
      post.user=request.user
      post.diff=form.cleaned_data['date_to']-form.cleaned_data['date_from']

      post.save()  
      return redirect('app_task:task-dashboard', )
    
  context={'form':form,'datarec':data}
  return render(request,'app_task/update-Task-record.html',context)

def get_from_file_serial(mkey=None):
  qs =FileSerials.objects.filter(serial_name=mkey).values('next_serial_number')
  prev_val = qs[0]['next_serial_number']
  print(f'prev_val  :   {type(prev_val)} , {prev_val}'  )

  FileSerials.objects.filter(serial_name=mkey).update(next_serial_number=prev_val+1)

  newval =FileSerials.objects.filter(serial_name=mkey).values('next_serial_number')
  
  print(f' prev_val{prev_val}, newval: {newval}')

  
  return prev_val
def post_entries(request):
  if request.user.user.post_task:
    data= TaskTable.objects.all().order_by('is_posted','-created')   
    if request.method=='POST' :
      # getting idlist of boxes that are selected
      id_list = request.POST.getlist('boxes')
      print(f'id_list : {id_list}')     

      # get new serial
      mserial = get_from_file_serial('Task List')
      print(f'new serial {mserial}')
      unique_key = generate_posting_refno(mserial)
      posting_datetime = datetime.now()       

      # update record        
      for x in id_list:  
        mdata = TaskTable.objects.filter(pk=int(x)).update(is_posted=True,date_posted = posting_datetime, posted_serial=unique_key)

      return redirect('app_task:post-entries', )
    
    else:
      context={'data':data}
      return render(request,'app_task/post_entries.html',context)



  else:
    messages.success(request, 'You are not allowed to Post an Item')    
    return redirect('app_task:task-dashboard', )
  
def view_item(request,pk=None):
  print(f'pk is {pk}')
  data = get_object_or_404(TaskTable, pk=pk)
  short_description = data.task_desc
  context={'data':data}
  return render(request, "app_task/incident.html", context)
