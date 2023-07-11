from django.shortcuts import render
from django.http import HttpResponse
from .models import Article
from django.views import generic

class IndexView(generic.ListView):
    model = Article
    context_object_name = 'articles'
 
class DetailView(generic.DetailView):
    model = Article

def index(request):
    return HttpResponse('Hello Django')

def detail(request, id):
    return HttpResponse('detail ' + str(id))

def create(request):
    return HttpResponse('create')

def update(request, id):
    return HttpResponse('update ' + str(id))

def delete(request, id):
    return HttpResponse('delete ' + str(id))
# Create your views here.
