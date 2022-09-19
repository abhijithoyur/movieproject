from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import MovieForm
from .models import Movie

def index(request):
    movie=Movie.objects.all()
    content={
        'movie_info':movie
    }
    return render(request,'index.html',content)
def detail(request,movie_id):
    movie=Movie.objects.get(id=movie_id)
    return render(request,"detial.html",{'movie':movie})
def add_movie(request):
    if request.method=="POST":
        name=request.POST.get('name')
        description = request.POST.get('description')
        year = request.POST.get('year')
        img = request.FILES['img']
        movie=Movie(name=name,description=description,year=year,img=img)
        movie.save()

    return render(request,'add.html')
def update(request,id):
    movie=Movie.objects.get(id=id)
    form=MovieForm(request.POST or None,request.FILES,instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'movie':movie})


def delete(request, id):
    if request.method =='POST':
        movie = Movie.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request,'delete.html')

