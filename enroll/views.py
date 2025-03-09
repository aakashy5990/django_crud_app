from django.shortcuts import render,redirect
from .forms import StudentRegistration
from .models import User
from django.contrib import messages

# Create your views here.
def index(request):
    if request.method=="POST":
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pas = fm.cleaned_data['password']
            mess = fm.cleaned_data['message']
            reg = User(name=nm,email=em,password=pas,message=mess)
            reg.save()
            messages.info(request, 'You Data is stored in Database!!!')
            fm = StudentRegistration()
    else:
        fm = StudentRegistration()
    return render(request,'enroll/index.html',{'forms':fm})

def showdata(request):
    stud = User.objects.all()
    return render(request,'enroll/showdata.html',{'stu':stud})

    
#updatation login code
def update(request,id):
    if request.method == "POST":
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
            messages.info(request,'Your datais store in database')
    else:
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(instance=pi)
    return render(request,'enroll/update.html',{'forms':fm})        


# deletion logic 
def delete(request,id):
    if request.method == "POST":
        pi = User.objects.get(pk=id)
        pi.delete()        
        return redirect('show')