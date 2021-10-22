from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .models import Movie
from .forms import MovieForm
# Create your views here.


def index(request):
    movie = Movie.objects.all()
    context = {
        'movies_list' : movie
    }
    return render(request, 'index.html', context)


def detail(request,id):
    movie = Movie.objects.get(id=id)
    return render(request, 'detail.html',{'movie' : movie})


def add_movie(request):
    if request.method == 'GET':
        return render(request, 'add.html')
    
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        year = request.POST.get('year')
        image = request.FILES['image']
        
        movie = Movie(name=name, desc=description, year=year, img=image)
        movie.save()
        return redirect('/')
    
    
    
def update(request,id):
    movie = Movie.objects.get(id=id)
    form = MovieForm(request.POST or None, request.FILES or None, instance=movie)
    if request.method == 'GET':
        return render(request, 'edit.html',{'movie' : movie , 'form' : form})
    
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('/')
        
        else:
            return render(request, 'edit.html',{'movie' : movie , 'form' : form})
        
        
        
        
def delete(request,id):
    movie = Movie.objects.get(id=id)
    if request.method == 'POST':
        movie.delete()
        return redirect('/')
    
    return render(request, 'delete.html',{'movie' :movie})
    