from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from user.models import *
from user.forms import *
# Create your views here.
# this function is used to add and show data
def add_show(request):
    data=userinfo.objects.all()
    if request.method=='POST':
        form=userinfo_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add')
    else:
        form=userinfo_form()
    return render(request,'addshow.html',{'data':data,'form':form})

# update function
def update(request,id):
    if request.method=='POST':
        id=userinfo.objects.get(pk=id) # pk = primary key
        a=userinfo_form(request.POST, instance=id)
        if a.is_valid():
            a.save()
    else:
        id=userinfo.objects.get(pk=id) # pk = primary key
        a=userinfo_form(instance=id)
    return render(request,'update.html',{'form':a})

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('add')
        else:
            messages.info(request,'invalid user and password')
            return redirect('login')
    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('addshow')
