from django import forms
from app_query.models import Teacher,Task, Employee, Position
#Enrollment,Student, Course

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

class EmployeeForm(forms.ModelForm):
  gender_choices = [
      ('Male','Male'),
      ('Female','Female')
  ]   
  emp_name = forms.CharField(
      max_length=50,
      label='Employee Name',
      required=True,
      

      widget=forms.TextInput(attrs={'class':'form-control','placeholder':'fullname'}), 
      # initial='Name',
  )
  emp_email = forms.EmailField(
      
      label='Employee Email',
      
      widget=forms.EmailInput(attrs={'class':'form-control','type':'email', 'placeholder':'example@1.com'}
                              ) 
  )    
  emp_gender =  forms.ChoiceField(
     choices=gender_choices,
     widget=forms.Select(attrs={'class': 'form-control'})
  )
  # many to many fields
  emp_position = forms.ModelMultipleChoiceField(
     label='Position',
     queryset = Position.objects.all().order_by('position_name'),
     widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-control'})
  )



  class Meta :
    model = Employee
    fields=('emp_name', 'emp_email', 'emp_gender' , 'emp_position' )