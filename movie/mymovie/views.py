from django.shortcuts import render

# Create your views here.

def nav(request):
    return render(request,'1.html')

def home(request):
    return render(request,'2.html')

def about(request):
    return render(request,'3.html')

def contact(request):
    return render(request,'4.html')

def form(request):
    n=request.GET.get("name")
    e=request.GET.get("email")
    a=request.GET.get("age")
    data={"name":n,"email":e,"age":a}
    return render(request,'form.html',data)