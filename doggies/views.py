from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
    return render(request, 'doggies/index.html')

def search(request):
    return render(request, 'doggies/search.html')

def filter(request):
    return render(request, 'doggies/filter.html')
