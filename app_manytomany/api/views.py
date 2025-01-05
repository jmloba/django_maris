from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from  app_manytomany.models import Students, Modules
from .serializer import StudentsSerializer, ModulesSerializer

class StudentsViewSet(viewsets.ModelViewSet):
  serializer_class = StudentsSerializer
  def get_queryset(self):
    student = Students.objects.all()
    return student
  def create(self, request,*args,**kwargs):
    data = request.data()
    new_student = Students.objects.create(
      studno=data['studno'], 
      name=data['name'], 
      grade = data['grade'],
      birthdate = data['birthdate'],
      )
    new_student.save()
    for module in data['modules']:
      module_obj = Modules.objects.get(module_name=module['module_name'])
      new_student.modules.add(module_obj) 

    serializer = StudentsSerializer(new_student)  
    return Response(serializer.data)

  
class ModulesViewSet(viewsets.ModelViewSet):
  serializer_class = ModulesSerializer
  def get_queryset(self):
    module = Modules.objects.all()
    return module
