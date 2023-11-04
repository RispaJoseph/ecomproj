from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth
from django.views.decorators.cache import cache_control

# Create your views here.

def reg(request):
    if request.method == 'POST':
        uname=request.POST['uname']
        uemail=request.POST['uemail']
        upass=request.POST['pass']
        cpasswd=request.POST['cpass']
        if(upass!=cpasswd):
            messages.info(request,'Password does not match.')
        elif User.objects.filter(username=uname).exists():
            messages.info(request,'Username already exists.')
        elif User.objects.filter(email=uemail).exists():
            messages.info(request,'Email is taken.')
        else:
            new_user=User.objects.create_user(username=uname,email=uemail,password=upass)
            new_user.save()

            new_user1=Users.objects.create(uname=uname,uemail=uemail,upass=upass)
            new_user1.save()

            return redirect('login')
    return render(request,"reg.html")

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def login(request):
    if 'username' in request.session:
        return redirect('index')
    if request.method == 'POST':
        uname=request.POST['uname']
        passwd=request.POST['pass']
        u=auth.authenticate(username=uname,password=passwd)
        if u is None:
            messages.info(request,'Invalid credentials.')
        else:
            request.session['username']=uname
            return redirect('index')
    return render(request,"login.html")

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def index(request):
    if 'username' in request.session:
        uname=request.session['username']
        return render(request,"home/index.html",{'uname':uname})
    return redirect('login')

def logout(request):
    if 'username' in request.session:
        request.session.flush()
    return redirect('login')

