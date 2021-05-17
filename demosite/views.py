from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def map(request):
    return render(request,'map.html')

def technology(request):
    return render(request,'technology.html')

def ask(request):
    return render(request,'ask.html')