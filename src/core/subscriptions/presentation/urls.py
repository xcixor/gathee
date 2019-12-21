from django.urls import path
from subscriptions.presentation.auth.login import login_request
from subscriptions.presentation.index.index import index
from subscriptions.presentation.auth.logout import logout_request
from subscriptions.presentation.auth.account import account_view
from subscriptions.presentation.auth.signup import signup_view
from subscriptions.presentation.courses.courses import (
    courses_view, go_to_course, send_course_request)
from subscriptions.presentation.lessons.lessons import course_lesson
from subscriptions.presentation.about.about_page import about_page
from subscriptions.presentation.contact.contact_page import contact


app_name = 'subscriptions'

urlpatterns = [
    path('', index, name='index'),
    path('login', login_request, name='login'),
    path('logout', logout_request, name='logout'),
    path('account', account_view, name='account'),
    path('signup', signup_view, name='signup'),
    path('courses', courses_view, name='courses'),
    path('course/<int:course_id>', go_to_course, name='course'),
    path('purchase_course/<int:course_id>', send_course_request, name='purchase_course'),
    path('lesson/<int:lesson_id>', course_lesson, name='lesson'),
    path('about', about_page, name='about'),
    path('contact', contact, name='contact')
]