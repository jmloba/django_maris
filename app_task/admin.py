from django.contrib import admin

# Register your models here.

from .models import TaskCategory , TaskTable, FileSerials
# Register your models here.
class TaskCategoryAdmin(admin.ModelAdmin):
  list_display=('name',)
  ordering=('name',)
  list_editable =()
  filter_horizontal=()
  list_filter =()
  fieldsets=()

class TaskTableAdmin(admin.ModelAdmin):
  list_display=('user','category','task_desc','date_from','date_to','diff', 'doc_img','created', 'updated','posted_serial','is_posted','date_posted')
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

admin.site.register(TaskCategory, TaskCategoryAdmin)

admin.site.register(TaskTable, TaskTableAdmin)
admin.site.register(FileSerials, FileSerialsAdmin)