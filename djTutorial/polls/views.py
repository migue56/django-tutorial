# Create your views here.
from django.http import HttpResponse
from .models  import Question
from django.shortcuts import get_object_or_404, render



def index(request):
    lastest_question_list = Question.objects.order_by('pib_date')[:5]
    #output= ','.join([q.question_text for q on lastest_question_list])
    #return HttpResponse(output)
    #template = loader.get_template('polls/index.html')
    context = {'lastest_question_list': lastest_question_list}
    #return HttpResponse(template.render(context,request))
    return render(request,"apps/polls/index.html",context)


def detail(request,question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'apps/polls/detail.html', {'question': question})


def results(request,question_id):
    response = "You're looking at results of questions %s"
    return HttpResponse(response %question_id)

def vote (request,question_id):
    return HttpResponse("You're voting on queston %s" % question_id)
    