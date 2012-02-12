from django.shortcuts import render_to_response
from django.template import RequestContext
from project.main.models import *
from django.http import HttpResponseBadRequest, Http404, HttpResponseRedirect

from project.results.models import *

def index(request):
    surveys = Survey.objects.all()
    return render_to_response("index.html",{'surveys':surveys},RequestContext(request))

def take_survey(request):
    sid = request.GET.get("sid")
    if not sid:
        return HttpResponseBadRequest("Could not find survey")
    if request.method=="POST":
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
            
            return render_to_response("thank_you.html",{'sid':sid},RequestContext(request))
        
        except Survey.DoesNotExist:
            return HttpResponseBadRequest("Could not find survey")
        except Question.DoesNotExist:
            return HttpResponseBadRequest("Could not find one of the questions")        
    else:
        survey = Survey.objects.get(id=sid)
        return render_to_response("survey.html",{'survey':survey},RequestContext(request))



def create_survey(request):
    survey = Survey()
    survey.save()
    return HttpResponseRedirect("/edit/survey/?sid=%s" % survey.id)

def edit_survey(request):
    sid = request.GET.get("sid")
    if not sid:
        return HttpResponseBadRequest("No Survey found")
    
    try:
        survey = Survey.objects.get(id=sid)
        if request.method=="POST":
            new_name = request.POST.get("survey-name")
            if new_name:
                survey.name = new_name
                survey.save()
        return render_to_response("edit_survey.html",{'survey':survey},RequestContext(request))
    except Survey.DoesNotExist:
        return HttpResponseBadRequest("No Survey Found")

def publish_survey(request):
    sid = request.GET.get("sid")
    if not sid:
        return HttpResponseBadRequest("No Survey found")
    try:
        survey = Survey.objects.get(id=sid)
        survey.is_published = True
        survey.save()
        return render_to_response("publish_survey.html",{'survey':survey},RequestContext(request))
    except Survey.DoesNotExist:
        return HttpResponseBadRequest("Could not find the survey")


def create_question(request):
    sid = request.GET.get("sid")
    if not sid:
        return HttpResponseBadRequest("No Survey found")
    if request.method=="POST":
        try:
            survey = Survey.objects.get(id=sid)
            text = request.POST.get("question-text")
            question = TextQuestion(text=text,survey=survey)
            question.save()
            return HttpResponseRedirect("/edit/survey/?sid=%s" % sid)

        except Survey.DoesNotExist:
            return HttpResponseBadRequest("No Survey Found")        
    else:
        return render_to_response("create_question.html",{'sid':sid},RequestContext(request))

def dashboard(request):
    sid = request.GET.get("sid")
    if not sid:
        return HttpResponseBadRequest("No Survey found")
    try:
        survey = Survey.objects.get(id=sid)
        survey_results = survey.results.all()
        return render_to_response("dashboard.html",{'survey':survey},RequestContext(request))
    except Survey.DoesNotExist:
        return HttpResponseBadRequest("Survey could not be found")

    
def view_survey(request):
    sid = request.GET.get("sid")
    if not sid:
        return HttpResponseBadRequest("No Survey found")
    try:
        survey = Survey.objects.get(id=sid)
        return render_to_response("view_survey.html",{'survey':survey},RequestContext(request))

    except Survey.DoesNotExist:
        return HttpResponseBadRequest("No Survey Found")

def view_meta(request):
    sid = request.GET.get("sid")
    if not sid:
        return HttpResponseBadRequest("No Survey found")
    try:
        survey = Survey.objects.get(id=sid)        
        return render_to_response("view_meta.html",{'survey':survey},RequestContext(request))
    except Survey.DoesNotExist:
        return HttpResponseBadRequest("No survey found")

def view_all_surveys(request):
    surveys = Survey.objects.all()
    return render_to_response("view_all_surveys.html",{'surveys':surveys},RequestContext(request))
