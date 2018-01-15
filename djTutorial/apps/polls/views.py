# Create your views here.
from django.http import HttpResponse
from .models  import Question
from django.template import loader
from django.shortcuts import render


def index(request):
    lastest_question_list = Question.objects.order_by('pib_date')[:5]
    #output= ','.join([q.question_text for q on lastest_question_list])
    #return HttpResponse(output)
    #template = loader.get_template('polls/index.html')
    context = {'lastest_question_list': lastest_question_list}
    #return HttpResponse(template.render(context,request))
    return render(request,'polls/index.html',context)


def detail(request,question_id):
    return HttpResponse("You're looking at question %s.",question_id)


def results(request,question_id):
    response = "You're looking at results of questions %s"
    return HttpResponse(response % question_id)

def vote (request,question_id):
    return HttpResponse("You're voting on queston %s" % question_id)
    