from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout
from .models import student
# Create your views here.

def home(request):
    data=student.objects.all()
    return render(request,"home.html",{"data":data})

def user_login(request):

    if request.method=="POST":
        form=AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            return redirect("home")
    else:
        form=AuthenticationForm()
    return render(request,"login.html",{"form":form})

def user_logout(request):
    logout(request)
    return redirect("login")

def form(request):
    if request.method=="POST":
        name=request.POST.get("name")
        roll=request.POST.get("rollno")
        enroll=request.POST.get("enroll")
        dob=request.POST.get("date")
        title=request.POST.get("title")
        student.objects.create(name=name,roll_no=roll,enrollment=enroll,DOB=dob,title=title)
        return redirect("home")
    return render(request,"form.html")