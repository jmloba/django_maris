from rest_framework import serializers
from app_manytomany.models import Students, Modules

class ModulesSerializer(serializers.ModelSerializer):
  class Meta:
    model = Modules
    fields =['id','module_name','module_duration','class_room']


class StudentsSerializer(serializers.ModelSerializer):
  class Meta:
    model = Students
    fields =['id','studno','name','grade','birthdate','modules']
    depth = 1
    

