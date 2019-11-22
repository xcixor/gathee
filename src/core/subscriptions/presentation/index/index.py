from django.shortcuts import render
from subscriptions.presentation.auth.forms import LoginForm

def index(request):
    """Renders the homepage"""
    login_form = LoginForm()
    context = {'form': login_form}
    return render(request, 'index/index.html', context)