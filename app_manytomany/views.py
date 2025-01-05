from django.http import JsonResponse
from django.shortcuts import render,redirect
from app_manytomany.models import Students, Modules
from app_manytomany.forms import StudentForm
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

def StudentDashboard(request):
  data= Students.objects.all()
  form = StudentForm()
  context = {'Student_data':data, 'form':form }
  return render(request,'app_manytomany/student-dashboard.html',context)
  
def StudentAddNewRecord(request):
  form= StudentForm()

  
  if request.method =='POST':
    if form.is_valid():
      form.save()
      return redirect('app_manytomany:StudentDashboard')

  context= {'form': form}
  return render (request,'app_manytomany/student_addrecord.html', context)

def view_relate(request,pk):
  if request.method== 'GET':
    print(f'view others ')

    # try :
    #   data= Students.objects.get(pk=pk)
    # except ObjectDoesNotExist :
    #   response ={'status': 'failed', 'message':  f'record : {pk} does not exist'  }
    #   return JsonResponse(response)
    

    # modules =[]
    # for  position in data.modules.all():
    #   dta = {position}
    #   modules.append(position)
    #   # print(f'module position : {position}')
    # print(f'modules : {modules}')  

    response ={'status': 'success', 'message':  f'{pk}'  }
    return JsonResponse(response)


