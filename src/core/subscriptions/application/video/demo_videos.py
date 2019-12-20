"""Fetch demo videos."""
from subscriptions.models.video.video_models import (
    PremiumVideoDemo, LessonVideoDemo)


def get_premium_demo_videos():
    """Fetches demo videos.
    returns videos(list)
    """
    video_list = PremiumVideoDemo.objects.all()
    return video_list


def get_lesson_demo_video(lesson):
    """
    Fetches the demo videos of a lesson

    args:
        lesson(object): the demo's lesson

    returns:
        video(object): the lesson's demo video
    """
    demo = LessonVideoDemo.objects.filter(lesson=lesson).first()
    return demo
