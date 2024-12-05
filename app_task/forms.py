
from django import forms
from .models import TaskTable
from formtools.preview import FormPreview

class DateInput(forms.DateInput):
  input_type = 'date'

class TaskTableForm(forms.ModelForm):
  date_from = forms.DateTimeField(
    widget = forms.DateTimeInput(
      attrs={
        'class':'form-control', 
        'type': 'datetime-local',
      }
    )
  )
  date_to = forms.DateTimeField(
    widget = forms.DateTimeInput(
      attrs={
        'class':'form-control', 'type': 'datetime-local'
      }
    )
  )

  class Meta :
    model = TaskTable
    fields=('category','task_desc','date_from','date_to','doc_img')
    
class DeleteRecordTaskForm(forms.ModelForm) :
  class Meta :
    model = TaskTable
    fields=('user','category','task_desc','date_from','date_to','doc_img')
    labels={
      'user':'User:',
      'category':'Category:',
      'task_desc':'Description',
      'date_from':'Date(from)',
      'date_to':'Date(to)',
      'doc_img':'Document',
    }   
  def __init__(self,*args,**kwargs):
    super(DeleteRecordTaskForm,self).__init__(*args,**kwargs)
    self.fields['user'].disabled=True    
    self.fields['category'].disabled=True
    self.fields['task_desc'].disabled=True
    self.fields['date_from'].disabled=True    
    self.fields['date_to'].disabled=True     
    self.fields['doc_img'].disabled=True       

class UpdateRecordTaskForm(forms.ModelForm) :
  date_from = forms.DateTimeField(
    widget = forms.DateTimeInput(
      attrs={
        'class':'form-control', 
        'type': 'datetime-local',
      }
    )
  )
  date_to = forms.DateTimeField(
    widget = forms.DateTimeInput(
      attrs={
        'class':'form-control', 'type': 'datetime-local'
      }
    )
  )  
  class Meta :
    model = TaskTable
    fields=('user','category','task_desc','date_from','date_to','doc_img')
