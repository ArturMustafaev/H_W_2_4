from django.shortcuts import render
from main.models import Product
from main.models import Director
from main.models import Movie
from main.models import Review

# Create your views here.

def index(request):
    dict_={
        'key': "Hello World",
        'color': '#05fc89',
        'list_': ['Artur', 'Django', 'Python']
    }
    return render(request, 'index.html', context=dict_)



def product_list_view(request):
    products = Product.objects.all()
    context = {
        'product_list': products
    }
    print(products)
    return render(request, 'products.html', context=context)

def product_detail_view(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'detail.html', context={'product': product})


def director_films(request):
    director = Director.objects.all()
    context = {
        'director_list': director
    }
    return render(request, 'Films.html', context=context)


def director_film(request, id):
    director = Director.objects.get(id=id)
    return render(request, 'director.html', context={'director': director})

def movies_film(request):
    movies = Movie.objects.all()
    context = {
        'movies_list': movies
    }
    return render(request, 'film.html', context=context)

def movies_films(request, id):
    movie = Movie.objects.get(id=id)
    return render(request, 'movie.html', context={'movie': movie})

def review(request):
    review = Review.objects.all()
    context = {
        'review_list': review
    }
    return render(request, 'review.html', context=context)

def review_list(request, id):
    review = Movie.objects.get(id=id)
    return render(request, 'rewiev_.html', context={'review': review})