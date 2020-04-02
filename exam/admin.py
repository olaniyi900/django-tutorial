from django.contrib import admin
from .models import Choice, Question

class ChoiceAdmin(admin.TabularInline):
    model = Choice



class QuestionAdmin(admin.ModelAdmin):
    models = Question
    inlines = [ChoiceAdmin]
    

admin.site.register(Question, QuestionAdmin)
