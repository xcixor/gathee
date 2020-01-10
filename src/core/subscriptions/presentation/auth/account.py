from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from subscriptions.application.contact.contact import get_address_info


@login_required
def account_view(request):
    """Renders the user's dashboard."""
    return render(request, 'auth/account.html', {'address': get_address_info})