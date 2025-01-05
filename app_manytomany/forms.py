from django import forms
from app_manytomany.models import Students, Modules

class StudentForm(forms.ModelForm):
  class Meta :
    model = Students
    fields = ('studno','name','grade','birthdate', 'modules')