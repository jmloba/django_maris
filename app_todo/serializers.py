

from rest_framework import serializers

from .models import Task_Todo
from django import forms


class  TaskTodoSerializer( serializers.ModelSerializer):
  class Meta:
    model = Task_Todo
    fields=('title','completed')

