#from django.http import HttpResponse
#from django.template import loader
#from django.http import Http404
#from django.shortcuts import render
from django.shortcuts import get_object_or_404, render


from .models import Question

# def index(request, question_id):
    #return HttpResponse("hello,world.You're at the polls index."question_id)

#def results(request, question_id):
    #response = "You're looking at the results of question %s."
    #return HttpResponse(response % question_id)

#def vote(request, questiion_id):
    #return HttpResponse("You're voting on question %s. % questiion_id")

#def index(request):
    #latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #output = ','.join([q.question_text for q in latest_question_list])
    #return HttpResponse(output)
    #template = loader.get_template('polls/index.html')
    #context = {
        #'latest_question_list':latest_question_list,
    #}
    #return HttpResponse(template.render(context,request))
    #return render(request,'polls/index.html',context)
    #def detail(request, question_id):
        #try:
            #question = Question.objects.get(pk=question_id)
        #except Question.DoesNotExist:
            #raise Http404("Qustion does not exist")
        #return render(request, 'polls/detail.html',{'question':question})
    def detail(request, question_id):
        question = get_object_or_404(Question, pk=question_id)
        return render(request,'polls/dental.html',{'question':question})
