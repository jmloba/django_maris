from django import forms
from app_query.models import Teacher,Task

class TeacherForm(forms.ModelForm):    
  class Meta :
    model = Teacher
    fields = ('name',)
    
class TimeInput(forms.TimeInput):
    input_type = "time"

class TimeInput(forms.TimeInput):
    input_type = "time"


class TaskForm(forms.ModelForm):    
  task_date = forms.DateTimeField(
    widget = forms.DateTimeInput(
      attrs={
        'class':'form-control', 
        'type': 'date',
      }
    )
  )  
  start_time = forms.TimeField(
      widget = forms.TimeInput(
      attrs={
        'class':'form-control', 
        'type': 'time',
      }
    )
  )
  end_time = forms.TimeField(
      widget = forms.TimeInput(
      attrs={
        'class':'form-control', 
        'type': 'time',
        'format':'%H:%M'
      }
    )
  )

  class Meta :
    model = Task
    fields = ('owner','name','task_date','start_time','end_time')
  

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["start_time"].widget = TimeInput()
        self.fields["end_time"].widget = TimeInput()        