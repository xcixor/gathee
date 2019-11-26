from django.shortcuts import render
from subscriptions.presentation.auth.forms import LoginForm
from subscriptions.application.index.courses import get_courses

def index(request):
    """Renders the homepage"""
    login_form = LoginForm()
    courses = get_courses()
    context = {'form': login_form, 'courses': courses}
    return render(request, 'index/index.html', context)