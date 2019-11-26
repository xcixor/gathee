"""Defines the models for Courses."""
from django.db import models


class Courses(models.Model):
    title = models.CharField(max_length=40, null=False, blank=False, unique=True)

    def __str__(self):
        return self.title
