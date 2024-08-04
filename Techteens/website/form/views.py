from django.shortcuts import render
from .models import data
from .models import table

# Create your views here.
def index (request):
   return render(request,'index.html')

def about (request):
   return render(request,'about.html')

def session (request):
   return render(request,'session.html')

def visual (request):
   return render(request,'visual.html')
   
def tips (request):
   return render(request,'tips.html')

def contact (request):
   return render(request,'contact.html')

def base (request):
   return render(request,'base.html')

def new (request):
    if request.method=="POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        obj= data(name=name,email=email,message=message)
        obj.save()
    return render(request,'new.html')

def new2 (request):
   if request.method=="POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        obj= table(name=name,email=email,message=message)
        obj.save()
   return render(request,'new2.html')


