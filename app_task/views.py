from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render,redirect
from .models import TaskTable,FileSerials, TaskHistory,MFO, MFOsub,MFOsub2

from django.db.models import ExpressionWrapper, F, fields, Func
from app_accounts.models import UserAccess
from .forms import TaskTableForm,UpdateRecordTaskForm, TaskHistoryForm,DeleteRecordHistoryForm, DeleteRecordTaskForm,DeleteRecordMFOForm, DeleteRecordMFOsubForm,DeleteRecordMFOsub2Form,MFOForm,MFOsubForm,MFOsubForm2
from app_task.reportlab_task_template import get_task_to_print
from app_task.reportlab_simpledoc import using_simpledoc
from django.utils.timezone import timedelta
import datetime
from django.contrib import messages
from app_task.utils import generate_posting_refno
from datetime import datetime


def task_Dashboard(request):
  user_access = UserAccess.objects.get(user=request.user)
  form = TaskTableForm()

  if user_access.supervisor:
    data = TaskTable.objects.all().order_by('mfo','mfosub','mfosub2')
    
  else:  
    data = TaskTable.objects.filter(user=request.user).order_by('mfo','mfosub','mfosub2')

  context={'data':data, "form":form,'user_access':user_access}
  return render(request,'app_task/task_Dashboard.html', context)
def create_taskref(request):
  ref=str(request.user)+'-'+str(datetime.now())
  return ref
def dashboard_mfo(request):
  data=MFO.objects.all().order_by('name')
  form = MFOForm()
  if request.method=='POST':
    form = MFOForm(request.POST or None)
    if form.is_valid():
 
      form.save()
      
      data=MFO.objects.all()
      context={'data':data, }

      return redirect('app_task:dashboard-mfo', )
    else:
      print(f'create_record  mfo form is not valid ')
      return redirect('app_task:dashboard-mfo' )
      

  context={'data':data, 'form':form }
  return render(request,'app_task/dashboard_mfo.html', context)

def dashboard_mfosub(request):
  data=MFOsub.objects.all().order_by('mfo__name','name')
  form = MFOsubForm()
  if request.method=='POST':
    form = MFOsubForm(request.POST or None)
    if form.is_valid():
 
      form.save()
      
      data=MFOsub.objects.all().order_by('-mfo','name')
      context={'data':data, }

      return redirect('app_task:dashboard-mfosub', )
    else:
      print(f'create_record  mfo form is not valid ')
      return redirect('app_task:dashboard-mfosub' )
        

  context={'data':data, 'form':form }
  return render(request,'app_task/dashboard_mfosub.html', context)
  
def dashboard_mfosub2(request):
  data=MFOsub2.objects.all().order_by('mfo__name','mfosub__name','name')
  form = MFOsubForm2()
  if request.method=='POST':
    form = MFOsubForm2(request.POST or None)
    if form.is_valid():
 
      form.save()
      
      data=MFOsub2.objects.all().order_by('-mfo','name')
      context={'data':data, }

      return redirect('app_task:dashboard-mfosub2', )
    else:
      print(f'create_record  mfo form is not valid ')
      return redirect('app_task:dashboard-mfosub2' )
        

  context={'data':data, 'form':form }
  return render(request,'app_task/dashboard-mfosub2.html', context)

def entry_mfo(request):
  pass

def create_record_modal(request):
  if request.method== 'POST':
    form = TaskTableForm(request.POST or None, request.FILES or None)
    
    
    if form.is_valid():
      print('form is valid')
      post = form.save(commit=False)
      post.diff=form.cleaned_data['date_to']-form.cleaned_data['date_from']
      # vars
      
      date_from=form.cleaned_data['date_from']
      date_to=form.cleaned_data['date_to']
      date_diff=form.cleaned_data['date_to']-form.cleaned_data['date_from']

      table_reference = create_taskref(request)
      post.task_ref =table_reference
      
 

      post.user=request.user
      post.save()  
      print(f'data is saved ....')

      historytable = TaskHistory()
      historytable.reference = get_object_or_404(TaskTable,   task_ref=table_reference
        )
      historytable.user=request.user
      historytable.description='first entry'
      historytable.date_from = date_from
      historytable.date_to = date_to
      historytable.diff = date_diff

      historytable.save()


      data=TaskTable.objects.all()
      context={'data':data, 'form':form }

      return redirect('app_task:task-dashboard', )
    else:
      print(f'form is not valid {form.errors}')
      

      print(f'invalid form ')
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

def mfo_delete_record(request,pk=None):
  data= MFO.objects.get(id=pk)
  form = DeleteRecordMFOForm(instance = data) 
  if request.method=='POST':
    data.delete()   
    return redirect('app_task:dashboard-mfo', )
  context={'form':form,'datarec':data}
  return render(request,'app_task/delete_mfo.html', context)

def mfosub_delete_record(request,pk=None,):
  data= MFOsub.objects.get(id=pk)
  print(f'data')
  form = DeleteRecordMFOsubForm(instance = data) 
  if request.method=='POST':
    data.delete()   
    return redirect('app_task:dashboard-mfosub', )
  context={'form':form,'datarec':data}
  return render(request,'app_task/delete_mfosub.html', context)

def mfosub2_delete_record(request,pk=None,):
  data= MFOsub2.objects.get(id=pk)
  print(f'data')
  form = DeleteRecordMFOsub2Form(instance = data) 
  if request.method=='POST':
    data.delete()   
    return redirect('app_task:dashboard-mfosub2', )

  context={'form':form,'datarec':data}
  return render(request,'app_task/delete_mfosub2.html', context)


def history_delete_record(request,pk=None, reference=None):
  print(f'\nhistory delete record :\nreference: {reference}  ')
  data= TaskHistory.objects.get(id=pk)
  form = DeleteRecordHistoryForm(instance = data) 
  if request.method=='POST':
    data.delete()   
    return redirect('app_task:task-dashboard' )
  
  context={'form':form,'datarec':data, "main_ref":reference}
  return render(request,'app_task/delete_task_history.html' , context)

def update_record(request, pk=None):
  data= TaskTable.objects.get(id=pk)
  form = UpdateRecordTaskForm(instance =data)
  if request.method=='POST':

    form = UpdateRecordTaskForm(request.POST or None,request.FILES or None, instance = data)
    if form.is_valid():  
      post = form.save(commit=False)
      post.user=request.user
      post.diff=form.cleaned_data['date_to']-form.cleaned_data['date_from']

      post.save()  
      return redirect('app_task:task-dashboard', )
    
  context={'form':form,'datarec':data}
  return render(request,'app_task/update-Task-record.html',context)

def history_update_record(request,pk=None,ref=None):
  data= TaskHistory.objects.get(id=pk)

  print(f'history update record - ref: {ref}')
  form = TaskHistoryForm(instance = data)

  if request.method=='POST':

    form = TaskHistoryForm(request.POST or None, instance = data)
    if form.is_valid():  
      form.save()

      return redirect('app_task:task-dashboard' )
    

  context={'form':form,'datarec':data,"main_reference":ref}
  return render(request,'app_task/update-history-record.html',context)


def get_from_file_serial(mkey=None):
  print(f'\n\nprocedure-->> get from file serial :')
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

def history_view(request,pk=None):
  print(f"history view-->> passed pk : {pk}")
  task = TaskTable.objects.get(pk=pk)
  print(f'task : {task}, {task.category}\npk is : {pk}')
  
  form = TaskHistoryForm( )
  data = TaskHistory.objects.filter(reference=task)
  record_number=len(data)

  if request.method== 'POST':
    form = TaskHistoryForm(request.POST )
        
    if form.is_valid():
      print('form is valid _--->>>>')
      post= TaskHistory( reference=task,
        date_from= form.cleaned_data['date_from']  ,             
        date_to= form.cleaned_data['date_to'],
        user=request.user,
        description=form.cleaned_data['description'],
        revision=form.cleaned_data['revision'],
        submitted=form.cleaned_data['submitted']
          )
      post.save()
      print(f'for posting save : {post}')
      data = TaskHistory.objects.filter(reference=task)

  context={'data':data,'task':task, 'form':form ,'record_number':record_number,'pkref':pk}
  return render(request, "app_task/history.html", context)

def create_history_record_modal(request):

  if request.method== 'POST':
    form = TaskHistoryForm(request.POST )
        
    if form.is_valid():
      print('form is valid _--->>>>')
      data=TaskHistory.objects.all()
      context={'data':data, 'form':form }
      return render(request, "app_task/history.html", context)

def ajax_load_MFOsub(request):
    mfo_id = request.GET.get('mfo_id')
    subdata = MFOsub.objects.filter(mfo_id=mfo_id).order_by('name')
    print(f'subdata filtered are : {subdata }')
    '''first solution '''
    # return render(request, 'app_task/MFOsub_dropdown_list_options.html', {'subdata': subdata})
    print(f"values are : {subdata.values('id','name')}")
    return JsonResponse(list(subdata.values('id','name')), safe=False)

def ajax_load_MFOsub2(request):
  print(f'\n\nmfo sub2 ajax ')
  mfosub_id = request.GET.get('mfosub_id')
  print(f'\nmfosub_id--->>> {mfosub_id}')
  subdata = MFOsub2.objects.filter(mfosub_id=mfosub_id).order_by('name')
  print(f'subdata filtered are : {subdata }')
  '''first solution '''
  # return render(request, 'app_task/MFOsub_dropdown_list_options.html', {'subdata': subdata})
  print(f"values are : {subdata.values('id','name')}")
  return JsonResponse(list(subdata.values('id','name')), safe=False)





def print_task(request):
  print(f'app_task to print')
  # calling reportlab_task_template
  # report1 = get_task_to_print(request)

  # calling simpledoc
  report1 = using_simpledoc(request)

  print(f'to print data : {report1}')

def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

def print_task_ajax(request):
  if is_ajax(request):
    print('ajax request')
    print_task(request)
    response = {'status':'Success', 'Message': 'ajax request'}
    return JsonResponse(response)

  else:
    print('not ajax request')
    response = {'status':'no', 'Message': 'not ajax request'}
    return JsonResponse(response)

    # context={'invoice_list':invoice_list ,'mypath':mypath  }
    # return render(request,'app_print/print-invoice.html' ,context ) 