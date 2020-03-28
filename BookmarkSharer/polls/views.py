from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from .models import Question


def index(req):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    result = ','.join([q.question_text for q in latest_question_list])
    return HttpResponse(result)


def details(req, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(req, question_id):
    return HttpResponse("You're looking at the results of question %s." % question_id)


def vote(req, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
