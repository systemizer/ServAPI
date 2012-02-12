from django.shortcuts import render_to_response
from django.template import RequestContext
from project.main.models import *
from django.http import HttpResponseBadRequest, Http404

from project.results.models import *

def index(request):
    return render_to_response("index.html",{},RequestContext(request))

def survey(request):
    if request.method=="POST":
        sid = request.GET.get("sid")
        if not sid:
            return HttpResponseBadRequest("Could not find survey")
        try:
            survey = Survey.objects.get(id=sid)
            survey_result = SurveyResult(survey=survey)
            survey_result.save()
            for key,value in request.POST.items():
                if key=="csrfmiddlewaretoken":
                    continue
                question = Question.objects.get(id=key)
                question_result = QuestionResult(question=question,survey_result=survey_result,answer=value)
                question_result.save()                
        
        except Survey.DoesNotExist:
            return HttpResponseBadRequest("Could not find survey")
        except Question.DoesNotExist:
            return HttpResponseBadRequest("Could not find one of the questions")

            
        #do something
        pass
    else:
        survey = Survey.objects.all()[0]
        return render_to_response("survey.html",{'survey':survey},RequestContext(request))

