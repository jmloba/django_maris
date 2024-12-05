
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponse

from django.utils.timezone import localdate
from django.db.models import Sum

# @login_required(login_url='app_accounts:login-view')
def home(request):

  
  context = {
  }
  return render(request,'home.html',context )