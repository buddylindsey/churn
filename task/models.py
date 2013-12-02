from django.db import models

from django_extensions.db.models import (
    TimeStampedModel, TitleSlugDescriptionModel)


class Task(TimeStampedModel, TitleSlugDescriptionModel):
    completion_date = models.DateTimeField(blank=True, null=True)
    due_date = models.DateTimeField(blank=True, null=True)


class Notes(TimeStampedModel):
    task = models.ForeignKey(Task, related_name='notes')
    description = models.TextField()
