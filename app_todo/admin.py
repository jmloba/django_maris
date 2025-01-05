from django.contrib import admin

# Register your models here.
from app_todo.models import Task_Todo

class Task_TodoAdmin(admin.ModelAdmin):
  list_display=('id','title','completed',)
  ordering=('created_at',)
  list_editable =('title','completed',)
  filter_horizontal=()
  list_filter =()
  fieldsets=()


admin.site.register(Task_Todo, Task_TodoAdmin)  