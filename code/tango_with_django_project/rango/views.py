from django.shortcuts import render

from django.http import HttpResponse
from votreg.models import Category
from votreg.forms import MyForm

def index(request):
    # return HttpResponse("Rango says hey there world!")
    return HttpResponse(<html><body><a href = '/rango/about'>About</a></body></html>)
    

def about(request):
	return HttpResponse("Rango says here is the about page.")
	# <a href="/rango/">Index</a>

