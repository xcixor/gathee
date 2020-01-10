from django.shortcuts import render
from subscriptions.application.auth.forms import LoginForm
from subscriptions.application.courses.courses import get_courses
from subscriptions.application.video.demo_videos import get_premium_demo_videos
from subscriptions.application.contact.contact import get_address_info


def index(request):
    """Renders the homepage"""
    login_form = LoginForm()
    courses = get_courses()
    demo_videos = get_premium_demo_videos()
    context = {
        'form': login_form,
        'courses': courses,
        'demo_videos': demo_videos,
        'address': get_address_info
        }
    return render(request, 'index/index.html', context)