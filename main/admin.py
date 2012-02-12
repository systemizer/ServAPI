from project.main.models import *
from django.contrib import admin


admin.site.register(Survey)
admin.site.register(TextQuestion)
admin.site.register(BooleanQuestion)
admin.site.register(MultipleChoiceQuestion)


