from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(req):
    return HttpResponse("Hello World ! You're at the polls app index.")


def details(req, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(req, question_id):
    return HttpResponse("You're looking at the results of question %s." % question_id)


def vote(req, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
