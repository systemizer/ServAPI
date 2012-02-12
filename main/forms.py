from project.main.models import *
from django import forms


class TextQuestionForm (forms.ModelForm):
    class Meta:
        model = TextQuestion

