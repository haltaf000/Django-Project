from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, "website/index.html")

def haider(request):
    return HttpResponse("Hello, Haider")

def greet(request, name):
    return HttpResponse(f"Hello, {name.capitalize()}!")