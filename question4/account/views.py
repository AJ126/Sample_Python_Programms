from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
# Create your views here.
def login(request):
    if request.method=='POST':
        password=request.POST['password']
        username=request.POST['username']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('index')
        else:
            messages.info(request,'invalid user and password')
            return redirect('login')
    else:
        return render(request,'login.html')

def register(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        password=request.POST['password']
        password1=request.POST['password1']
        email=request.POST['email']
        if password==password1:
            if User.objects.filter(username=username).exists():
               messages.info(request,'username is already taken')
               return redirect('register')
            elif User.objects.filter(email=email).exists():
               messages.info(request,'email is exists')
               return redirect('register')
            else:
               user=User.objects.create_user(username=username, password=password1, email=email,first_name=first_name, last_name=last_name)
               user.save()
               return redirect('login')
        else:
           messages.info(request,'password is not matching')
           return redirect('register')
        return redirect('/')
    else:
       return render(request,'register.html')

def logout(request):
    auth.logout(request)
    return redirect('index')
