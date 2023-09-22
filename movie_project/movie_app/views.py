from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import Movieform
from .models import Movies


# Create your views here.
def index(request):
    movie = Movies.objects.all()
    context = {'movie_list': movie}
    return render(request, 'index.html', context)


def detail(request, movie_id):
    movie = Movies.objects.get(id=movie_id)
    return render(request, 'Detail.html', {'movie': movie})


def add(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        description = request.POST.get("desc")
        year = request.POST.get("year")
        image = request.FILES['img']
        movie = Movies(name=name, desc=description, year=year, img=image)
        movie.save()
    return render(request, 'add.html')

def update(request, id):
    movie = Movies.objects.get(id=id)
    form = Movieform(request.POST or None, request.FILES, instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'update.html', {'form': form, 'movie': movie})

def delete(request, id):
    if request.method == 'POST':
        movie = Movies.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request, 'delete.html')
