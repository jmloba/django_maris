from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
from django.utils import formats
from django.core.validators import  MinValueValidator, MaxValueValidator

class TaskCategory(models.Model):
  name =  models.CharField(max_length=40, blank=True, null=True)
  def __str__(self):
    return self.name

class MFO(models.Model):
  name=models.CharField(max_length=100, null = True, blank = True, unique=True)
  def __str__(self):
    return str(self.name)
  
class MFOsub(models.Model):
  mfo = models.ForeignKey(MFO, on_delete=models.CASCADE)
  name= models.CharField(max_length=100, null=True, blank=True)
  def __str__(self):
    return str(self.name)
  
class MFOsub2(models.Model):
  mfo = models.ForeignKey(MFO, on_delete=models.CASCADE)
  mfosub = models.ForeignKey(MFOsub, on_delete=models.CASCADE)  
  name= models.CharField(max_length=100, null=True, blank=True)
  def __str__(self):
    return str(self.name)  

class TaskTable(models.Model):
  task_ref = models.CharField(max_length=50, null=True,blank=True)

  mfo= models.ForeignKey(MFO, on_delete=models.SET_NULL, null=True)

  mfosub= models.ForeignKey(MFOsub, on_delete=models.SET_NULL, null=True)
  mfosub2= models.ForeignKey(MFOsub2, on_delete=models.SET_NULL, null=True)

  user = models.ForeignKey(User, on_delete=models.CASCADE, null=True,blank=True) 

  category=models.ForeignKey(TaskCategory,on_delete=models.CASCADE, null=True,blank=True)
  task_desc = models.TextField(blank=True,null=True)

  date_from = models.DateTimeField(null=True, blank=True)
  date_to = models.DateTimeField(null=True, blank=True)

  diff = models.DurationField(null=True, blank=True)  
  created=models.DateTimeField(auto_now_add=True, null=True)  
  updated = models.DateTimeField(auto_now=True)
  
  doc_img = models.ImageField(upload_to='doc_images/', null=True,blank=True)

  posted_serial= models.CharField(max_length=30, blank=True, null=True)
  is_posted= models.BooleanField(default = False)  
  date_posted = models.DateTimeField(null=True, blank=True)  

  
  def __str__(self):
    return str(self.task_ref)

  def format_date_from (self):
    return self.date_from.strftime("%Y/%m/%d %H:%M:%S")  
  
  def format_date_to (self):
    return self.date_to.strftime("%Y/%m/%d %H:%M:%S")  
  
class TaskHistory(models.Model):
  user=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
  reference = models.ForeignKey(TaskTable,on_delete=models.CASCADE, max_length=20,blank = True,null=True,related_name='history')

  date_from = models.DateTimeField(null=True, blank=True)
  date_to = models.DateTimeField(null=True, blank=True)  
  diff = models.DurationField(null=True, blank=True)    

  description=models.CharField(max_length=200, null=True, blank=True)
  revision=models.BooleanField(default=False)
  submitted=models.BooleanField(default=False)
  created=models.DateTimeField(auto_now_add=True, null=True)  


  def format_created (self):
    return self.created.strftime('%Y/%m/%d')

  def format_date_from (self):
    return self.date_from.strftime("%Y/%m/%d %H:%M:%S")
  
  def format_date_to (self):
    return self.date_to.strftime("%Y/%m/%d %H:%M:%S")  
  
class FileSerials(models.Model) :
  user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True) 
  serial_name =  models.CharField(max_length=30, blank=True, null=True)
  next_serial_number = models.IntegerField( blank=True, null=True,
        validators=[MinValueValidator(1), MaxValueValidator(100000)])
  
  def __str__(self):
    return self.serial_name  

