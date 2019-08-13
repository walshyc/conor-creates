from django.contrib import admin
from polls.models import poll_question, poll_choice

admin.site.register(poll_question)
admin.site.register(poll_choice)