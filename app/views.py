from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def log (request):
    return HttpResponse ('<center> <h1> Login Sucessfull !!! </h> </center> ')
