from django.shortcuts import render,redirect
from .models import Department,Student
import csv
from io import TextIOWrapper
# Create your views here.
def home(request):
    return render(request,"home.html")

def show_stu(request):
    data=Student.objects.all()
    return render(request,"show_stu.html",{"data":data})

def upload_csv(request):
    if request.method=="POST":
        csv_file=request.FILES["csv1.file"]
        file=TextIOWrapper(csv_file.file,encoding='utf-8')
        reader=csv.reader(file)
        next(reader)
        for i in reader:
            name=i[0]
            enroll=i[1]
            email=i[2]
            dept_name=i[3]
            dept,created=Department.objects.get_or_create(dept=dept_name,defaults={'hod':'Unknown'})
            Student.objects.create(name=name,enroll=enroll,email=email,dept=dept)

        return redirect('show_stu')
    return render(request,"upload.html")