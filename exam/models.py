from django.db import models

class Question(models.Model):
    question_name = models.CharField(max_length=150)

    def __str__(self):
        return self.question_name

class Choice(models.Model):
    choice_text = models.CharField(max_length=150)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.choice_text
    
    
