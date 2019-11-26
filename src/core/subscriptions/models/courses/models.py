"""Defines the models for Courses."""
from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=40, null=False, blank=False, unique=True)
    description = models.CharField(max_length=500, null=True, blank=True)
    course_image = models.ImageField(null=True, upload_to="images/courses/")

    def __str__(self):
        return self.title
