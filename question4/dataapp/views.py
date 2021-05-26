from django.shortcuts import render, redirect
from dataapp.models import *
from dataapp.forms import *
# Create your views here.
def addcandidate(request):
    if request.method=='POST':
        form=candidateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form=candidateForm()
    return render(request,'addcandidate.html',{'form':form})

def showcandidate(request):
    data=candidate.objects.all()
    return render(request,'showcandidate.html',{'data':data})

def update(request,id):
    if request.method=='POST':
        id=candidate.objects.get(pk=id) # pk = primary key
        a=candidateForm_1(request.POST, instance=id)
        if a.is_valid():
            a.save()
            return redirect('showcandidate')
    else:
        id=candidate.objects.get(pk=id) # pk = primary key
        a=candidateForm_1(instance=id)
    return render(request,'update.html',{'form':a})
