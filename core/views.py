from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(requesr):
    return HttpResponse('<h1>Welcome To Social Book</h1>')