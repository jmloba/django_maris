from django.contrib import admin

# Register your models here.

from .models import TaskCategory , TaskTable, FileSerials, TaskHistory,MFO,MFOsub,MFOsub2
# Register your models here.
class TaskCategoryAdmin(admin.ModelAdmin):
  list_display=('name',)
  ordering=('name',)
  list_editable =()
  filter_horizontal=()
  list_filter =()
  fieldsets=()

class TaskTableAdmin(admin.ModelAdmin):
  list_display=('task_ref','user','mfo','mfosub','mfosub2','category','task_desc','date_from','date_to','diff', 'doc_img','created', 'updated','posted_serial','is_posted','date_posted',)
  ordering=('user','created','category')
  list_editable =('category','doc_img','date_from','date_to','posted_serial','is_posted','date_posted')
  filter_horizontal=()
  list_filter =()
  fieldsets=()

class FileSerialsAdmin(admin.ModelAdmin):
  list_display=('user','serial_name','next_serial_number',)
  ordering=('serial_name',)
  list_editable =('serial_name','next_serial_number',)
  filter_horizontal=()
  list_filter =()
  fieldsets=()

class TaskHistoryAdmin(admin.ModelAdmin):
  list_display=('user','revision','submitted','reference','created','description','date_from','date_to','diff')
  ordering=('reference',)
  list_editable =('description','revision','submitted')
  filter_horizontal=()
  list_filter =()
  fieldsets=()

class MFOAdmin(admin.ModelAdmin):
  list_display=('name',)
  ordering=('name',)
  list_editable =()
  filter_horizontal=()
  list_filter =()
  fieldsets=()  


class MFOsubAdmin(admin.ModelAdmin):
  list_display=('mfo','name')
  ordering=('mfo','name')
  list_editable =('name',)
  filter_horizontal=()
  list_filter =()
  fieldsets=()   

class MFOsub2Admin(admin.ModelAdmin):
  list_display=('mfo','mfosub','name')
  ordering=('mfo','name')
  list_editable =('name','mfosub')
  filter_horizontal=()
  list_filter =()
  fieldsets=()     

admin.site.register(MFOsub2, MFOsub2Admin)
admin.site.register(MFOsub, MFOsubAdmin)

admin.site.register(MFO, MFOAdmin)
admin.site.register(TaskHistory, TaskHistoryAdmin)

admin.site.register(TaskCategory, TaskCategoryAdmin)

admin.site.register(TaskTable, TaskTableAdmin)
admin.site.register(FileSerials, FileSerialsAdmin)