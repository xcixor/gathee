"""Contains courses related with the dashboard."""
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def dashboard_view(request):
    """Renders the user's dashboard."""
    return render(request, 'dashboard/dashboard.html')