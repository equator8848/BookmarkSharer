from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(req):
    return HttpResponse("Hello World ! You're at the polls app index.")


