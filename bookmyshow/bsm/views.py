from django.shortcuts import redirect, render
from .models import Movie
# Create your views here.

def home(request):
    return render(request,"home.html")

def add(request):
    name=request.GET.get('name')
    drname=request.GET.get('director')
    rating=request.GET.get('rating')
    date=request.GET.get('date')
    data={
        "n":name,
        "dr":drname,
        "rating":rating,
        "date":date
    }
    if name and drname and rating and date:
        Movie.objects.create(
                name=name,
                director=drname,
                rating=rating,
                date=date
            )

        return redirect("show")
    return render(request,"add.html")   

def show(request):

    search=request.GET.get("search")
    if search:
        d1=Movie.objects.filter(name__icontains=search)
    else:
        d1=Movie.objects.all()
    d2={"d1":d1,"se":search}

    # movies = Movie.objects.all()

    # data = {
    #     "movies": movies
    # }

    return render(request,"show.html",d2)