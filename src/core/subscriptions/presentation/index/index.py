from django.shortcuts import render
from subscriptions.presentation.auth.forms import LoginForm
from subscriptions.application.index.courses import get_courses
from subscriptions.application.index.demo_videos import get_demo_videos

def index(request):
    """Renders the homepage"""
    login_form = LoginForm()
    courses = get_courses()
    demo_videos = get_demo_videos()
    context = {'form': login_form, 'courses': courses, 'demo_videos': demo_videos}
    return render(request, 'index/index.html', context)