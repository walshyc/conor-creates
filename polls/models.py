from django.db import models

class poll_question(models.Model):
    question_text = models.CharField(max_length = 90)
    publication_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

class poll_choice(models.Model):
    question = models.ForeignKey(poll_question, on_delete = models.CASCADE)
    choice_text = models.CharField(max_length = 150)
    votes = models.IntegerField(default = 0)

    def __str__(self):
        return self.choice_text
