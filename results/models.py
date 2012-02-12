from django.db import models
from project.main.models import *

class SurveyResult(models.Model):
    survey = models.ForeignKey(Survey,related_name="results")
    
    
class QuestionResult(models.Model):
    question = models.ForeignKey(Question,related_name="question_result")
    survey_result = models.ForeignKey(SurveyResult,related_name="survey_questions")
    answer = models.CharField(max_length=128)
