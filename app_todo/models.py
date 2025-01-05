from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task_Todo(models.Model):
  title = models.CharField(max_length=100, blank=True, null=True )
  completed = models.BooleanField(default =False, blank = True, null = True)
  user = models.ForeignKey(User, on_delete=models.CASCADE, null=True,blank=True)
  created_at = models.DateTimeField(auto_now_add=True, null=True)
  updated_at = models.DateTimeField(auto_now=True, null=True)
  def __str__(self):
    return  f'{self.title}'