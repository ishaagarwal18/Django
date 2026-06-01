from django.shortcuts import render,HttpResponse

# Create your views here.

def ipl(request):
    return render(request,"ipl.html")

def home(request):
    data={"name":"Isha","age":20,"Hobby":"Cricket",
          "Marks":[20,21,22,23,24,25]}
    return render(request,"1.html",{"new":data})

def table(request):
    table={
        "Subject":["DM","Python","FSD","TOC","COA"],
        "Marks":[23,24,21,8,21]
    }
    data2=[{
        "Subject":s,
        "Marks":m,
    }
    for s,m in zip(table["Subject"],table["Marks"])]
    return render(request,"table.html",{"test":data2})