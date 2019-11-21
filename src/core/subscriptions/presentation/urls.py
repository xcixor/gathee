from django.urls import path
from subscriptions.presentation.auth.login import login_request
from subscriptions.presentation.index.index import index
from subscriptions.presentation.auth.logout import logout_request
from subscriptions.presentation.dashboard.dashboard import dashboard_view


app_name = 'subscriptions'

urlpatterns = [
    path('', index, name='index'),
    path('login', login_request, name='login'),
    path('logout', logout_request, name='logout'),
    path('dashboard', dashboard_view, name='dashboard')
]