

from rest_framework import serializers

from app_query.models import Employee, Position, Task
from  app_task.models import TaskTable


class  EmployeeSerializer( serializers.ModelSerializer):
  class Meta:
    model = Employee
    fields ='__all__'


class  PositionSerializer( serializers.ModelSerializer):
  class Meta:
    model = Position
    fields ='__all__'


class  TaskSerializer( serializers.ModelSerializer):
  class Meta:
    model = Task
    fields ='__all__'

class  TaskTableSerializer( serializers.ModelSerializer):
  class Meta:
    model = TaskTable
    fields ='__all__'
