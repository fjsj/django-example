#coding=utf-8

from django.db import models

from model_utils.models import TimeStampedModel


class Note(TimeStampedModel):
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['-created']
