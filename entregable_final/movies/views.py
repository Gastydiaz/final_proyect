from django.shortcuts import render
from movies.models import Movies,Studio,Director,Windows
from movies.forms import MoviesForm,StudioForm,DirectorForm
from django.views.generic import DeleteView


def index(request):
    window =Windows.objects.filter(name__contains='index')
    context = {
        'window':window[0]
    }
    return render(request, 'index.html', context=context)


def create_movie(request):
    if request.method == 'GET':
        context = {
            'form': MoviesForm()

        }
        return render(request,'create_movies.html',context=context)

    elif request.method == 'POST':
        form = MoviesForm(request.POST, request.FILES)
        if form.is_valid():
            Movies.objects.create(
                name=form.cleaned_data['name'],
                type=form.cleaned_data['type'],
                duration=form.cleaned_data['duration'],
                picture = form.cleaned_data['picture'],
                premiered = form.cleaned_data['premiered'],
                date = form.cleaned_data['date']
            )
            context = {
                'message' : 'Pelicula creada exitosamente'
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
    context = {
        'movies':all_movies,
    }
    return render(request,'list_movies.html',context=context)


def movie_update(request, pk):
    movie = Movies.objects.get(id=pk)

    if request.method == 'GET':
        context = {
            'form': MoviesForm(
                initial={
                    'name':movie.name,
                    'type':movie.type,
                    'duration':movie.duration,
                    'picture':movie.picture,
                    'premiered':movie.premiered,
                    'date':movie.date,
                }
            )
        }

        return render(request, 'update_movies.html', context=context)

    elif request.method == 'POST':
        form = MoviesForm(request.POST, request.FILES)
        if form.is_valid():
            movie.name = form.cleaned_data['name']
            movie.type = form.cleaned_data['type']
            movie.duration = form.cleaned_data['duration']
            movie.picture = form.cleaned_data['picture']
            movie.premiered = form.cleaned_data['premiered']
            movie.date = form.cleaned_data['date']
            movie.save()
            
            context = {
                'message': 'Pelicula actualizada exitosamente'
            }
        else:
            context = {
                'form_errors': form.errors,
                'form': MoviesForm()
            }
        return render(request, 'update_movies.html', context=context)


class MovieDeleteView(DeleteView):
    model = Movies
    template_name = 'delete_movies.html'
    success_url = '/movies/list-movies/'





def create_studio(request):
    if request.method == 'GET':
        context = {
            'form': StudioForm()

        }
        return render(request,'create_studios.html', context=context)

    elif request.method == 'POST':
        form = StudioForm(request.POST, request.FILES)
        if form.is_valid():
            Studio.objects.create(
                name=form.cleaned_data['name'],
                creation=form.cleaned_data['creation'],
                place=form.cleaned_data['place'],
                image = form.cleaned_data['image'],
                
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


def studio_update(request, pk):
    studio = Studio.objects.get(id=pk)

    if request.method == 'GET':
        context = {
            'form': StudioForm(
                initial={
                    'name':studio.name,
                    'creation':studio.creation,
                    'place':studio.place,
                    'image':studio.image,
                    
                }
            )
        }

        return render(request, 'update_studios.html', context=context)

    elif request.method == 'POST':
        form = StudioForm(request.POST, request.FILES)
        if form.is_valid():
            studio.name = form.cleaned_data['name']
            studio.creation = form.cleaned_data['creation']
            studio.place = form.cleaned_data['place']
            studio.image = form.cleaned_data['image']
            studio.save()
            
            context = {
                'message': 'Estudio actualizado exitosamente'
            }
        else:
            context = {
                'form_errors': form.errors,
                'form': StudioForm()
            }
        return render(request, 'update_studios.html', context=context)


class StudioDeleteView(DeleteView):
    model = Studio
    template_name = 'delete_studio.html'
    success_url = '/movies/list-studio/'


def create_director(request):
    if request.method == 'GET':
        context = {
            'form': DirectorForm()

        }
        return render(request,'create_director.html',context=context)

    elif request.method == 'POST':
        form = DirectorForm(request.POST, request.FILES)
        if form.is_valid():
            Director.objects.create(
                name=form.cleaned_data['name'],
                films=form.cleaned_data['films'],
                birth=form.cleaned_data['birth'],
                photo=form.cleaned_data['photo'],
                retired=form.cleaned_data['retired'],
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


def director_update(request, pk):
    director = Director.objects.get(id=pk)

    if request.method == 'GET':
        context = {
            'form': DirectorForm(
                initial={
                    'name':director.name,
                    'films':director.films,
                    'birth':director.birth,
                    'photo':director.photo,
                    'retired':director.retired,
                    
                }
            )
        }

        return render(request, 'update_director.html', context=context)

    elif request.method == 'POST':
        form = DirectorForm(request.POST, request.FILES)
        if form.is_valid():
            director.name = form.cleaned_data['name']
            director.films = form.cleaned_data['films']
            director.birth = form.cleaned_data['birth']
            director.photo = form.cleaned_data['photo']
            director.retired = form.cleaned_data['retired']
            director.save()
            
            context = {
                'message': 'Director actualizado exitosamente'
            }
        else:
            context = {
                'form_errors': form.errors,
                'form': DirectorForm()
            }
        return render(request, 'update_director.html', context=context)



class DirectorDeleteView(DeleteView):
    model = Director
    template_name = 'delete_director.html'
    success_url = '/movies/list-director/'



def about_me(request):
    return render(request,'about_me.html',context={})



