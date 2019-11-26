"""Defines the models for videos."""
from django.db import models
from subscriptions.models.courses.models import Courses


class Video(models.Model):
    name = models.CharField(max_length=600, null=False, blank=False, unique=True)
    video_file = models.FileField(upload_to='videos', null=True, verbose_name="Select Video:")
    course = models.ForeignKey(
        Courses, related_name='videos', on_delete=models.SET_NULL,
        null=True, blank=True)

    def __str__(self):
        return self.name + ": " + str(self.video_file)
