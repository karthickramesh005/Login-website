from django.shortcuts import render,redirect
from .models import *
# Create your views here.
def InsertPageView(request):
    return render(request,"insert.html")

def InsertData(request):
    fname = request.POST['fname']
    lname = request.POST['lname']
    Email = request.POST['Email']
    Pass = request.POST['contact']

    newuser = Student.objects.create(Firstname=fname,Lastname=lname,Email=Email,Number=Pass)

    return redirect('showpage')

def ShowPage(request):
    all_data = Student.objects.all()
    return render(request,"show.html",{'key1':all_data})

def EditPage(request,pk):
    get_data = Student.objects.get(id=pk)
    return render(request,"edit.html",{'key2':get_data})

def UpdateData(request,pk):
    udata = Student.objects.get(id=pk)
    udata.Firstname = request.POST['fname']
    udata.Lastname = request.POST['lname']
    udata.Email = request.POST['Email']
    udata.Number = request.POST['contact']

    udata.save()

    return redirect('showpage')

def DeleteData(request,pk):
    ddata = Student.objects.get(id=pk)

    ddata.delete()
    return redirect('showpage')