from django.shortcuts import render
from django.http import HttpResponse
from movies.models import Movies,Studio,Director
from movies.forms import MoviesForm,StudioForm,DirectorForm


def index(request):
    return render(request, 'index.html', context={})


def create_movie(request):
    if request.method == 'GET':
        context = {
            'form': MoviesForm()

        }
        return render(request,'create_movies.html',context=context)

    elif request.method == 'POST':
        form = MoviesForm(request.POST)
        if form.is_valid():
            Movies.objects.create(
                name=form.cleaned_data['name'],
                type=form.cleaned_data['type'],
                duration=form.cleaned_data['duration'],
            )
            context = {
                'message' : 'Pelicula creada existosamente'
            }
            return render(request,'create_movies.html',context=context)
        else:
            context ={
                'form_errors' : form.errors,
                'form' : MoviesForm(),
            }
            return render(request,'create_movies.html',context=context)

        
        

def list_movies(request):
    if 'search' in request.GET:
        search = request.GET['search']
        all_movies =Movies.objects.filter(name__contains=search)
    else:
        all_movies =Movies.objects.all() 
    print(all_movies)
    context = {
        'movies':all_movies,
    }
    return render(request,'list_movies.html',context=context)


def create_studio(request):
    if request.method == 'GET':
        context = {
            'form': StudioForm()

        }
        return render(request,'create_studios.html', context=context)

    elif request.method == 'POST':
        form = StudioForm(request.POST)
        if form.is_valid():
            Studio.objects.create(
                name=form.cleaned_data['name'],
            )
            context = {
                'message' : 'Estudio creado exitosamente'
            }
            return render(request,'create_studios.html',context=context)
        else:
            context ={
                'form_errors' : form.errors,
                'form': StudioForm(),
            }
            return render(request,'create_studios.html',context=context)


def list_studio(request):
    if 'search' in request.GET:
        search = request.GET['search']
        all_studios =Studio.objects.filter(name__icontains=search)
    else:
        all_studios =Studio.objects.all() 
    context = {
        'studios':all_studios,
    }
    return render(request,'list_studio.html',context=context)

def create_director(request):
    if request.method == 'GET':
        context = {
            'form': DirectorForm()

        }
        return render(request,'create_director.html',context=context)

    elif request.method == 'POST':
        form = DirectorForm(request.POST)
        if form.is_valid():
            Director.objects.create(
                name=form.cleaned_data['name'],
                films=form.cleaned_data['films'],
            )
            context = {
                'message' : 'Director creado exitosamente'
            }
            return render(request,'create_director.html',context=context)
        else:
            context ={
                'form_errors' : form.errors,
                'form': DirectorForm(),
            }
            return render(request,'create_director.html',context=context)

def list_director(request):
    if 'search' in request.GET:
        search = request.GET['search']
        all_directors =Director.objects.filter(name__icontains=search)
    else:
        all_directors =Director.objects.all() 
    
    context = {
        'directors':all_directors,
    }
    return render(request,'list_director.html',context=context)