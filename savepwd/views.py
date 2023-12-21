
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Pwd,Customer
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.

def index(request):
  template = loader.get_template('homepage.html')
  return HttpResponse(template.render({},request))

def loginUser(request):
  if request.method == 'POST':
    uname = request.POST.get('uname')
    pwd = request.POST.get('pwd')
    user = authenticate(request,username= uname, password=pwd)
    if user is not None:
      login(request,user)
      return redirect('home')
  context = {}
  return render(request, 'login.html', context)

def logoutUser(request):
  logout(request)
  return redirect('index')

def register(request):
  form = UserCreationForm()
  if request.method == 'POST':
     form = UserCreationForm(request.POST)
     if form.is_valid():
       form.save()
       return redirect('home')
  context = {'form':form}
  return render(request,'register.html', context)
  

@login_required(login_url='index')
def pwdpage(request):
   mypwd = Pwd.objects.all().values()
   template = loader.get_template('asg.html')
   context = {
    'mypwd': mypwd,
  }
   return HttpResponse(template.render(context, request))

@login_required(login_url='index')
def add(request):
  template = loader.get_template('add.html')
  return HttpResponse(template.render({}, request))

@login_required(login_url='index')
def addrecord(request):
  x = request.POST['sname']
  y = request.POST['paswd']
  pwd = Pwd(sname = x, paswd = y)
  pwd.save()
  return HttpResponseRedirect(reverse('index'))

@login_required(login_url='index')
def delete(request, id):
  pwd = Pwd.objects.get(id=id)
  pwd.delete()
  return HttpResponseRedirect(reverse('index'))

@login_required(login_url='index')
def update(request, id):
  mypwd = Pwd.objects.get(id=id)
  template = loader.get_template('update.html')
  context = {
    'mypwd': mypwd,
  }
  return HttpResponse(template.render(context, request))

@login_required(login_url='index')
def updaterecord(request, id):
  site = request.POST["site"]
  pd = request.POST["pd"]
  mypwd = Pwd.objects.get(id=id)
  mypwd.sname = site
  mypwd.paswd= pd
  mypwd.save()
  return HttpResponseRedirect(reverse('index'))

 

