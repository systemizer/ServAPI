from django.db import models
from django.contrib.auth.models import User
from django.template import Context,Template

from project.main.constants import *

class Survey(models.Model):
    name = models.CharField(max_length=128,default="Untitled")
    created = models.DateTimeField(auto_now_add=True)
    deleted = models.BooleanField(default=False)
    creator = models.ForeignKey(User,related_name="authored_surveys",null=True,blank=True) #for hackathon time reasons
    is_published = models.BooleanField(default=False)

    def get_all_questions(self):
        questions = []
        for q in BooleanQuestion.objects.filter(survey=self):
            questions.append(q)
        for q in TextQuestion.objects.filter(survey=self):
            questions.append(q)
        for q in MultipleChoiceQuestion.objects.filter(survey=self):
            questions.append(q)

        questions = sorted(questions,key=lambda q: q.id)
        return questions
        

class Question(models.Model):
    template = BASE_QUESTION_TEMPLATE

    survey = models.ForeignKey(Survey,related_name="questions")
    text = models.TextField()

    def render(self):
        t = Template(self.template)
        context = self.get_context()
        return t.render(context)

    def get_context(self):
        context = {'survey':self.survey,'text':self.text,'id':self.id}
        return Context(context)

    def get_type(self):
        return "Text"

    
class TextQuestion(Question):
    pass


class BooleanQuestion(Question):
    template = BOOLEAN_QUESTION_TEMPLATE

    def get_type(self):
        return "Checkbox"

    
class MultipleChoiceQuestion(Question):
    template = MULTIPLE_CHOICE_TEMPLATE
    choices = models.TextField() #comma seperated list of choices

#     def render(self):
#         t = Template(self.template)
#         context = self.get_context()
#         return t.render(context)

    def get_context(self):
        choices = self.choices.split(",")
        context = super(MultipleChoiceQuestion,self).get_context()
        context.update({'choices':choices})
        return context

    def get_type(self):
        return "Multiple Choice"

class MultipleCheckboxQuestion(MultipleChoiceQuestion):
    def get_type(self):
        return "Multiple Checkbox"



