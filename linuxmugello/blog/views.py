from  Connect import Connect
from .models import Choice, Question
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.shortcuts import render
import json
from django.http import JsonResponse
def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list, 'menu': Connect.menu(""), 'submenu': Connect.submnu(""), 'pagina':Connect.body("", "sanpiero"),'luogo':"sanpiero",'manifestazione':"news", 'news':Connect.news(""), 'urlx': " di Carlo Zanieri"}
    return render(request, 'blog/news.html', context)

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'blog/results.html'

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'blog/detail.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'blog/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('blog:results', args=(question.id,)))

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'blog/results.html', {'question': question})

def menu(request):
        menux=Connect.menu("")
        submenux=Connect.submnu("")
        context = {'menu': Connect.menu(""), 'submenu': Connect.submnu(""), 'mimetype':'application/json'}
        return render(request, 'blog/menu.html',context)
 
def newss(request):
                
        context = {'pagina':Connect.body("", "sanpiero"), 'manifestazione':"Blog", 'news':Connect.news(""), 'urlx':"html"}
        return render(request, 'blog/news.html',context)
  
def news_one(request):
        #titolo=request.POST['titolo']
        id=request.POST['id']
        context = {'pagina':Connect.body("", "sanpiero"), 'manifestazione':"news", 'news':Connect.news_one("",id)}
        return render(request, 'blog/news_one.html',context)
            
def slide(request):
        luogo="sanpiero"
        context = {'luogo' : luogo, 'slider':Connect.slider("", "index"),'menu': Connect.menu("")}
        return render(request, 'blog/nivo.html',context)      