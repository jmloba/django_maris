from django import forms
from app_todo.models import Task_Todo

class TodoForm(forms.ModelForm):
  class Meta :
    model = Task_Todo
    fields = ('title',)

