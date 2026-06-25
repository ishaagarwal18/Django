from django.shortcuts import render,get_object_or_404,redirect
from .models import Student
# Create your views here.

def display(request):
    data=Student.objects.all()
    return render(request,"1.html",{"new":data})

def update(request,id):
    d=get_object_or_404(Student,id=id)
    if request.method=="POST":
        d.Name=request.POST.get("Name")
        d.DOB=request.POST.get("DOB")
        d.enrollment=request.POST.get("enrollment")
        d.project_title=request.POST.get("project_title")
        d.save()
        return redirect("display")
    
    return render(request,"update.html",{"d":d})

def delete(request,id):
    f=get_object_or_404(Student,id=id)
    f.delete()
    return redirect("display")