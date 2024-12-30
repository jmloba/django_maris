from django.db import connection
from django.db.models import F,Q,Sum, Avg, Prefetch
from django.shortcuts import HttpResponse

from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render,redirect
from app_task.models import TaskTable, MFO, MFOsub,MFOsub2, TaskHistory

from app_query.models import Order,Customer,Product,LineItem, Book, Store, Posts, Author, Teacher,Classroom,Course,Student, Task

from django.views import  View
from app_task.forms import TaskTableForm
from app_query.forms import TeacherForm , TaskForm
from datetime import datetime

from django.contrib import messages 
from django.views.decorators.csrf import csrf_exempt
# from app_query.utils import is_ajax

# Create your views here.

from rest_framework.generics import CreateAPIView, ListAPIView

def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

def query_Dashboard(request):
  data = TaskTable.objects.filter(user=request.user).order_by('mfo','mfosub','mfosub2')
  form = TaskTableForm()
  context={'data':data,'form':form}
  return render(request,'app_query/query_Dashboard.html', context)

def create_taskref(request):
  ref=str(request.user)+'-'+str(datetime.now())
  return ref

def create_record_modal_qtest(request):
  if request.method== 'POST':
    form = TaskTableForm(request.POST or None, request.FILES or None)
    
    
    if form.is_valid():
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

      return redirect('app_query:query-dashboard', )
    else:

      data=TaskTable.objects.all()
      context={'data':data, 'form':form }

      return redirect('app_query:query-dashboard', )

# union example
def query_tasktable(request):
  # data = TaskTable.objects.all()
  

  # data = TaskHistory.objects.select_related('reference').order_by('reference','created').all() 

  # list=[item.reference for item in data]
  # print(f'\n\n data values :{data.values()}')
  # print(f'\n\nlist : {list}')
  

  books = Book.objects.all().prefetch_related('store_set')

  print(f'\n\nbooks :{books} **** {type(books)}')
  
  mbooks=[]
  for book in books:
    # print(f'\n\nbook: {book.bookname}'  )
    # print(f'book: {book.store_set.all()}'  )
    stores =book.store_set.all()
    for i in stores:
      # print(f'store {i.store_name}' )
      print(f' {book.bookname} , {i.store_name}, {book.price}  ')
      mbooks.append({book.bookname})
  print(f'mbooks : {mbooks}')


  # print(connection.queries)

  # context={'data':data,'store_data':stores, }


  context={'book_data':books,'mbooks':mbooks }

  return render(request,'app_query/query_Tasktable.html', context)
  

def query_classroom(request):
  teachers= Teacher.objects.all()
  teacherform= TeacherForm()
  context={'teachers':teachers,'teacherform':teacherform}
  return render(request,'app_query/query_classroom.html', context)


def add_record_teacher(request):
 if request.method== 'POST':
  form = TeacherForm(request.POST or None,)
  if form.is_valid():
    form.save()
    return redirect('app_query:query-classroom', )
  else:
    print('form is invalid - procadd_record_teacher')
    return redirect('app_query:query-classroom', )

def data_list_Teacher():
  mrec=Teacher.objects.all().values('id','name')
  mlist = list(mrec)
  return mlist

def data_list_Task():
  mrec=Task.objects.all().values('id','owner','name','task_date','start_time', 'end_time')
  mlist = list(mrec)
  print(f'mlist: {mlist}')
  return mlist

class UpdateDeleteTeacher_ajax(View):
  def get(self, request,pk,*args,**kwargs):
    if is_ajax(request):
      item = Teacher.objects.get(pk=pk)
      item.delete()
      response={"message":"success"}
      return JsonResponse(response)
    
    else :
      response={"message":"wrong route"}

      return JsonResponse(response)
 

def add_edit_record_teacher_ajax(request):
  if request.method== 'POST':
    print('add record teacher ajax ')
    form = TeacherForm(request.POST or None,)
    if form.is_valid():
      sid =  request.POST.get('stuid')
      if sid=='' or sid==None:
        doc = Teacher(
          name =request.POST.get('name'), 
                      )
      else:   
        doc = Teacher(
          id=sid,
          name =request.POST.get('name'), 
                      )
      doc.save()
      name = doc.name
      datalist=data_list_Teacher()
      response = {'status':'Success','name':name,'datalist':datalist}
      
      return JsonResponse(response)
    else:
      print('form is invalid ')
      response = {'status':'Failed',}
      return JsonResponse(response)

# ------------    
# query tables
# ------------    
def queryTableModal(request):
  
  task_table = Task.objects.all()
  task_form = TaskForm()


  context={'task_table':task_table,'task_form':task_form}
  return render(request,'app_query/query_tables.html', context)

#--- task table
def TaskAddEditRecord(request):
  if request.method== 'POST':
    print('request is post')
    
    form = TaskForm(request.POST or None,)
    if form.is_valid():
      sid =  request.POST.get('id')
      print(f'saving value of sid {sid}')
      if sid=='' or sid==None:
        doc = Task(
          owner =request.POST.get('owner'), 
          name =request.POST.get('name'), 
          task_date =request.POST.get('task_date'), 
          start_time =request.POST.get('start_time'), 
          end_time =request.POST.get('end_time'), 
          
                      )
      else:   
        doc = Task(
          id=sid,
          owner =request.POST.get('owner'), 
          name =request.POST.get('name'),  
                    task_date =request.POST.get('task_date'), 
          start_time =request.POST.get('start_time'), 
          end_time =request.POST.get('end_time'), 
                      )
      doc.save()

      name = doc.name
      datalist=data_list_Task()
      print(f'data is saved status --> success')
      response = {'status':'Success','name':name,'datalist':datalist}
      
      return JsonResponse(response)
    else:

      print(f'form is invalid {form.errors}')
      # messages.error(request, "Error")
      response = {'status':'Failed','messages':messages}
      return JsonResponse(response)


class updateDelete_modal2(View):
  form_class = TaskForm

  def get(self, request,pk,*args,**kwargs):
    if is_ajax(request):
      task = Task.objects.get(pk=pk)
      task.delete()
      data_list = data_list_Task()
      response = {'message': 'success','data_list':data_list}
      return JsonResponse(response)
    else:
      response = {'message': 'wrong route'}
      return JsonResponse(response)
    
  def post(self,request,pk, *args, **kwargs):
    if is_ajax(request):
      task = Task.objects.get(pk=pk)
      data={
        "owner": task.owner,
        "name" : task.name,
        "tassk_date" : task.task_date,
        "start_time" : task.start_time,
        "end_time" : task.end_time
      }

      form = self.form_class(request.POST)
      if form.is_valid():
        owner = form.cleaned_data['owner']
        name = form.cleaned_data['name']
        task_date = form.cleaned_data['task_date']
        start_time = form.cleaned_data['start_time']
        end_time = form.cleaned_data['end_time']
        if form.has_changed():

          task.owner= owner
          task.name = name
          task.task_dtae = task_date
          task.start_time = start_time
          task.end_time = end_time
          task.save()


          data_list=data_list_Task()

          response = {'message':'success', 'data_list':data_list}
          return JsonResponse(response)
        else:
          response = {'message':'data is not edited'}
          return JsonResponse(response)


      response ={'message': 'invalid form, Validation failed, wong request'}
      return JsonResponse(response)
    else :
      print('request is not ajax')



      
    response = {'message':'wrong request'}
    return JsonResponse(response)




  
