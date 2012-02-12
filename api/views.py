import json
from django.http import Http404, HttpResponse

from project.main.models import *
from project.results.models import * 

def fetch_survey(request):
    sid = request.GET.get("sid")
    if not sid:
        return Http404
    try:
        survey = Survey.objects.get(id=sid)
        output = {}
        output['survey_id'] = survey.id
        output['survey_name'] = survey.name
        output['questions'] = []

        questions = survey.questions.all()
        for question in questions:
            q = {}
            q['id'] = question.id
            q['num_results'] = question.question_results.count()
            q['answers'] = []
            for answer in question.question_results.all():
                r = {}
                r['answer'] = answer.answer
                r['survey_id'] = answer.survey_result.id

                q['answers'].append(r)

            output['questions'].append(q)
        
            

        return HttpResponse(json.dumps(output),mimetype="application/json")
        

    except Survey.DoesNotExist:
        return HttpResponseBadRequest("Could not find Survey")

                                                  
def fetch_question(request):
    qid = request.GET.get("qid")
    if not qid:
        return HttpResponseBadRequest("Could not find question")
    try:
        question = Question.objects.get(id=qid)
        output = {}
        output['id'] = qid
        output['num_answers'] = question.question_results.count()
        output['text'] = question.text
        output['survey_id'] = question.survey.id
        output['answers'] = []
        for answer in question.question_results.all():
            a = {}
            a['text'] = answer.answer
            a['id'] = answer.id
            output['answers'].append(a)
        return HttpResponse(json.dumps(output),mimetype="application/json")

    except Question.DoesNotExist:
        return HttpResponseBadRequest("Could not find question")
        
