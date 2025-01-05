from django.contrib import admin
from .models import Modules, Students, Modules
# Register your models here.

class ModulesAdmin(admin.ModelAdmin):  

  list_display=('module_name','module_duration','class_room',)
  ordering=('module_name',)
  list_editable =('module_duration','class_room',)
  filter_horizontal=()
  list_filter =()
  fieldsets=()   

admin.site.register(Modules,ModulesAdmin )  
admin.site.register(Students, )  