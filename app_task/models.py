from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User

from django.core.validators import  MinValueValidator, MaxValueValidator

class TaskCategory(models.Model):
  name =  models.CharField(max_length=40, blank=True, null=True)
  def __str__(self):
    return self.name


class TaskTable(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE, null=True,blank=True) 

  category=models.ForeignKey(TaskCategory,on_delete=models.CASCADE, null=True,blank=True)
  task_desc = models.TextField(blank=True,null=True)
  date_from = models.DateTimeField()
  date_to = models.DateTimeField()
  diff = models.DurationField(null=True, blank=True)  
  created=models.DateTimeField(auto_now_add=True, null=True)  
  updated = models.DateTimeField(auto_now=True)
  
  doc_img = models.ImageField(upload_to='doc_images/', null=True,blank=True)

  posted_serial= models.CharField(max_length=30, blank=True, null=True)
  is_posted= models.BooleanField(default = False)  
  date_posted = models.DateTimeField(null=True, blank=True)  
  
  def __str__(self):
    return str(self.category)
  
class FileSerials(models.Model) :
  user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True) 
  serial_name =  models.CharField(max_length=30, blank=True, null=True)
  next_serial_number = models.IntegerField( blank=True, null=True,
        validators=[MinValueValidator(1), MaxValueValidator(100000)])
  def __str__(self):
    return self.serial_name  

