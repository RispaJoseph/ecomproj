from django.shortcuts import render,redirect
from django.contrib import messages,auth
from django.contrib.auth.models import User
from django.views.decorators.cache import cache_control
# Create your views here.

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def admin_index(request):
    if 'username' not in request.session:
        return redirect('admin_login')
    result=User.objects.all().exclude(username='admin')
    return render(request,"index.html",{'result':result})

def edit_user(request,uid):
    user=User.objects.get(id=uid)
    if request.method == 'POST':
        user.username=request.POST['uname']
        user.email=request.POST['uemail']
        user.save()
        return redirect('admin_index')
    return render(request,"edit_user.html",{'user':user})

def search(request):
    query = request.GET.get('search', '')
    user = User.objects.filter(username=query) | User.objects.filter(email=query)
    params = {'result': user, 'query': query}

    if user.count() == 0:
        messages.warning(request, "Not Found")

    return render(request, "index.html", params)

def delete_user(request,uid):
    user=User.objects.get(id=uid)
    user.delete()
    return redirect('admin_index')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def admin_login(request):
    if 'username' in request.session:
        return redirect('admin_index')
    if request.method == 'POST':
        uname=request.POST['uname']
        passwd=request.POST['pass']
        u=auth.authenticate(username=uname,password=passwd)
        if u is None:
            messages.info(request,'Invalid credentials. P')
        elif uname!='admin1':
            messages.info(request,'Invalid credentials. Q')
        else:
            request.session['username']=uname
            return redirect('admin_index')
    return render(request,"login.html")

def admin_logout(request):
    if 'username' in request.session:
        request.session.flush()
    return redirect('login')