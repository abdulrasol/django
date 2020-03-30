from django.shortcuts import render
from django.http import HttpResponse  

# Create your views here.
def books(request):
    return HttpResponse('<h2>Welcome in our Book Site ^_^<h2>')
