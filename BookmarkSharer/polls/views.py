from django.shortcuts import render
from django.http import HttpResponse, Http404

# Create your views here.
from django.template import loader

from .models import Question


def index(req):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    return HttpResponse(template.render({'latest_question_list': latest_question_list}, req))


def details(req, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist !")
    return render(req, 'polls/details.html', {'question': question})


def results(req, question_id):
    return HttpResponse("You're looking at the results of question %s." % question_id)


def vote(req, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
