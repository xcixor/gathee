"""Fetch demo videos."""
from subscriptions.models.video.models import PremiumVideoDemo


def get_demo_videos():
    """Fetches demo videos.
    returns videos(list)
    """
    video_list = PremiumVideoDemo.objects.all()
    return video_list

