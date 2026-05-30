from django.shortcuts import render,HttpResponse

# Create your views here.

def hello1(request):
    return HttpResponse("hello")


def bye(request):
    return HttpResponse("bye")

def sayo(request):
    return HttpResponse("Sayonara")

def html1(request):
    return render(request,"scrollspy.html")


def html2(request):
    return render(request,"virat.html")


def html3(request):
    return render(request,"pseudo.html")
