from django.shortcuts import render
from .models import Grocery

# Create your views here.

def home(request):
    search=request.GET.get("search")
    if search:
        d1=Grocery.objects.filter(name__icontains=search)
    else:
        d1=Grocery.objects.all()

    return render(request, 'home.html',{"groceries":d1})
