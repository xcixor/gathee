from django.urls import path
from subscriptions.presentation.auth.login import login_request
from subscriptions.presentation.index.index import index
from subscriptions.presentation.auth.logout import logout_request
from subscriptions.presentation.auth.account import account_view


app_name = 'subscriptions'

urlpatterns = [
    path('', index, name='index'),
    path('login', login_request, name='login'),
    path('logout', logout_request, name='logout'),
    path('account', account_view, name='account')
]