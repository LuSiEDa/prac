"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.shortcuts import render
from django.urls import path
from django.http import HttpResponse

movie_list =[
    {'tittle':"파모","director":"장재현"},
    {'tittle':"영화2","director":"김감독"},
    {'tittle':"영화3","director":"이감독"},
    {'tittle':"영화4","director":"박감독"}
]

def index(request):
    return HttpResponse("<h1>Hello, world!</h1>")

def blog_list(request):

    book_text = ''
    for i in range(0, 10):
        book_text += f'book {i}<br>'
    return HttpResponse(book_text)

def book(request, num):
    book_text = f'book {num}번 페이지입니다.'
    return HttpResponse(book_text)


def language(request, lang):
    return HttpResponse(f'<h1>{lang}언어 페이지입니다.</h1>')

# 아까우니까 주석처리!
# def movies(request):
#     movie_titles = [
#         f'<a href="/movie/{index}/">{movie["tittle"]}</a>'
#         for index, movie in enumerate(movie_list)
#     ]
#
#     response_text = '<br>'.join(movie_titles)
#     return HttpResponse(response_text)

def movies(request):
    # from django.shortcuts import render
    return render(request,'movies.html',{'movie_list':movie_list})


def movie_detail(request, index):
    if index > len(movie_list) -1:
        from django.http import Http404
        raise Http404
    # movie = movie_list[index]
    # response_text = f'<h1>{movie["tittle"]}</h1> <p>감독 : {movie["director"]}</p>'
    context = {'movie_list': movie_list, 'index': index}
    return render(request, 'movie.html', context)

def gugu(request, num):
    context = {
        'num': num,
        'results':[num * i for i in range(1,10)]
    }
    return render(request, 'gugu.html', context)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('book_list/', blog_list),

    path('book/<int:num>/', book),
    path('language/<str:lang>/', language),
    path('movies/', movies),
    path('movie/<int:index>/', movie_detail),

    path('gugu<int:num>/', gugu),
]