"""Defines the models for videos."""
from django.db import models
from subscriptions.models.course.course_models import Course
from subscriptions.models.lesson.lesson_models import Lesson

class PremiumVideo(models.Model):
    name = models.CharField(max_length=150, null=False, blank=False, unique=True)
    video_file = models.FileField(upload_to='videos/premium', null=True, verbose_name="Select Video:")
    description = models.CharField(max_length=500, null=True, blank=False)
    course = models.ForeignKey(
        Course, related_name='videos', on_delete=models.SET_NULL,
        null=True, blank=True)

    class Meta:
        verbose_name_plural = "Premium Video Tutorials"

    def __str__(self):
        return self.name


class DemoVideo(models.Model):
    name = models.CharField(max_length=150, null=False, blank=False, unique=True)
    video_file = models.FileField(upload_to='videos/demo', null=True, verbose_name="Select Video:")


    class Meta:
            verbose_name_plural = "Demo Videos"

    def __str__(self):
        return self.name


class PremiumVideoDemo(models.Model):
    """Maps a demo to its video."""

    class Meta:
        verbose_name_plural = "Associate A video demo with its Course"
        unique_together = ('demo_video', 'premium_video')


    demo_video = models.ForeignKey(DemoVideo, on_delete=models.CASCADE, null=False, blank=False)
    premium_video = models.ForeignKey(PremiumVideo, on_delete=models.CASCADE, null=False, blank=False)

    def __str__(self):
        return str(self.demo_video.video_file)


class LessonVideo(models.Model):
    """
    Lesson's video
    """
    name = models.CharField(max_length=150, null=False, blank=False, unique=True)
    video_file = models.FileField(upload_to='lessons', null=True, verbose_name="Select Video:")
    description = models.CharField(max_length=500, null=True, blank=False)
    lesson = models.ForeignKey(
        Lesson, related_name='lesson_videos', on_delete=models.SET_NULL,
        null=True, blank=True)

    class Meta:
        verbose_name_plural = "Lesson Video Tutorials"
        unique_together = ('video_file', 'lesson')

    def __str__(self):
        return str(self.video_file)


class LessonVideoDemo(models.Model):
    """Creates a lesson demo video."""

    class Meta:
        verbose_name_plural = "Associate A video demo with its Lesson"
        unique_together = ('demo_video', 'lesson')

    demo_video = models.ForeignKey(DemoVideo, on_delete=models.CASCADE, null=False, blank=False)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, null=False, blank=False)

    def __str__(self):
        return str(self.demo_video.video_file)
