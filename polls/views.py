from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.http import HttpResponse
#from django.template import RequestContext, loader
from polls.models import Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    '''template = loader.get_template('polls/index.html')
    context = RequestContext(request, {'latest_question_list': latest_question_list,})'''
    context = {'latest_question_list': latest_question_list}
    '''output = ', '.join([p.question_text for p in latest_question_list])
    return HttpResponse(template.render(context))'''
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    '''try:
        question = Questio.objects.get(pk = question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")'''
    question = get_object_or_404(Question, pk = question_id)
    return render(request, 'polls/detail.html', {question : 'question'})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
