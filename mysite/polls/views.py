from django.http import HttpResponse, response

from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)


def detail(request, question_id):
    response = "You are looking at question %s."
    return HttpResponse(response % question_id)


def results(request, question_id):
    response = "You are looking at the result of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    response = "You are voting on question %s."
    return HttpResponse(response % question_id)
