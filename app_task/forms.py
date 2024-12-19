
from django import forms
from .models import TaskTable,TaskHistory, MFO, MFOsub,MFOsub2
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
    fields=('mfo','mfosub','mfosub2','task_desc',
            'date_from','date_to','doc_img',
            
            )
    labels={'mfo'      :'MFO',
            'mfosub'   :'MFO sub',
            'mfosub2'   :'MFO sub2',
            
            'date_from':'Date (from)','date_to'  :'Date (To)',
            'task_desc':'Description'
            }
    
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    # self.fields['mfo'].queryset = MFO.objects.all()
    self.fields['mfosub'].queryset = MFOsub.objects.none()
    
    self.fields['mfosub2'].queryset = MFOsub2.objects.none()    


    print(f'\n\nselfdata : {self.data}')
    # for mfosub
    if 'mfo' in self.data:
      print(f'mfo in self.data {self.data}')
      try:
        mfo_id= int(self.data.get('mfo'))
        print(f'\n\nin try mfoid is :{mfo_id}')

        self.fields['mfosub'].queryset=MFOsub.objects.filter(mfo_id=mfo_id).order_by('name')
      except(ValueError,TypeError) :
        pass 
    elif self.instance.pk:
      self.fields('mfosub').queryset=self.instance.mfo.name_set.order_by('name')


   # for mfosub2
    if 'mfosub' in self.data:
      print(f'mfo in self.data {self.data}')
      try:
        mfosub_id= int(self.data.get('mfosub'))
        print(f'\n\nin try mfoid is :{mfosub_id}')

        self.fields['mfosub2'].queryset=MFOsub2.objects.filter(mfosub_id=mfosub_id).order_by('name')
      except(ValueError,TypeError) :
        pass 
    elif self.instance.pk:
      self.fields('mfosub2').queryset=self.instance.mfosub.name_set.order_by('name')


class TaskHistoryForm(forms.ModelForm)    :
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
    model = TaskHistory
    fields=('date_from','date_to','description','revision','submitted',)

class MFOForm(forms.ModelForm):    
  class Meta :
    model = MFO
    fields = '__all__'

class MFOsubForm(forms.ModelForm):    
  class Meta :
    model = MFOsub
    fields = ('mfo', 'name' )    

class MFOsubForm2(forms.ModelForm):    
  class Meta :
    model = MFOsub2
    fields = ('mfo','mfosub', 'name' )    

  
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    # self.fields['mfo'].queryset = MFO.objects.all()
    self.fields['mfosub'].queryset = MFOsub.objects.none()
    


    print(f'\n\nselfdata : {self.data}')
    # for mfosub
    if 'mfo' in self.data:
      print(f'mfo in self.data {self.data}')
      try:
        mfo_id= int(self.data.get('mfo'))
        print(f'\n\nin try mfoid is :{mfo_id}')

        self.fields['mfosub'].queryset=MFOsub.objects.filter(mfo_id=mfo_id).order_by('name')
      except(ValueError,TypeError) :
        pass 
    elif self.instance.pk:
      self.fields('mfosub').queryset=self.instance.mfo.name_set.order_by('name')

class DeleteRecordTaskForm(forms.ModelForm) :
  class Meta :
    model = TaskTable
    fields=('user','mfo','mfosub','mfosub2','task_desc','date_from','date_to','doc_img')
    labels={
      'user':'User:',
      'mfo':'MFO',
      'mfosub':'MFO Sub',
      'mfosub2':'MFO Sub2',
      
      'task_desc':'Description',
      'date_from':'Date(from)',
      'date_to':'Date(to)',
      'doc_img':'Document',
    }  
  def __init__(self,*args,**kwargs):
    super(DeleteRecordTaskForm,self).__init__(*args,**kwargs)
    self.fields['user'].disabled=True    
    self.fields['mfo'].disabled=True    
    self.fields['mfosub'].disabled=True         
    self.fields['mfosub2'].disabled=True    
    self.fields['task_desc'].disabled=True    
    self.fields['date_from'].disabled=True         
    self.fields['date_to'].disabled=True         
    self.fields['doc_img'].disabled=True         


class DeleteRecordMFOForm(forms.ModelForm):
  class Meta :
    model = MFO
    fields=('name',)
    labels={
      'name':'Name',
    }   
  def __init__(self,*args,**kwargs):
    super(DeleteRecordMFOForm,self).__init__(*args,**kwargs)
    self.fields['name'].disabled=True    

class DeleteRecordMFOsubForm(forms.ModelForm):
  class Meta :
    model = MFOsub
    fields=('mfo','name',)
    labels={
      'mfo': 'MFO',
      'name':'Name',
    }   
  def __init__(self,*args,**kwargs):
    super(DeleteRecordMFOsubForm,self).__init__(*args,**kwargs)
    self.fields['mfo'].disabled=True    
    self.fields['name'].disabled=True    

class DeleteRecordMFOsub2Form(forms.ModelForm):
  class Meta :
    model = MFOsub2
    fields=('mfo','mfosub','name',)
    labels={
      'mfo': 'MFO',
      'mfosub': 'MFOsub',
      'name':'Name',
    }   
  def __init__(self,*args,**kwargs):
    super(DeleteRecordMFOsub2Form,self).__init__(*args,**kwargs)
    self.fields['mfo'].disabled=True    
    self.fields['mfosub'].disabled=True    
    self.fields['name'].disabled=True    

    
class DeleteRecordHistoryForm(forms.ModelForm) :
  class Meta :
    model = TaskHistory
    fields=('user','reference','date_from','date_to','description','revision','submitted')    
  def __init__(self,*args,**kwargs):
    super(DeleteRecordHistoryForm,self).__init__(*args,**kwargs)
    self.fields['user'].disabled=True    
    self.fields['reference'].disabled=True
    self.fields['date_from'].disabled=True
    self.fields['date_to'].disabled=True    
    self.fields['description'].disabled=True     
    self.fields['revision'].disabled=True       
    self.fields['submitted'].disabled=True       

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
    fields=('user','mfo','mfosub','mfosub2','task_desc','date_from','date_to','doc_img')
