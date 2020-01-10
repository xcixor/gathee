"""Fetch lesson videos."""
from subscriptions.models.video.video_models import (LessonVideo)


def get_lesson_video(lesson):
    """
    Fetch a lesson's video
    Args:
        lesson(object): The lesson to get its video
    Returns video(object): The lesson's video
    """
    if not LessonVideo.objects.filter(lesson=lesson):
        return False
    video = LessonVideo.objects.filter(lesson=lesson).first()
    return video
