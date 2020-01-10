from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from subscriptions.application.students.students_data import get_user_courses
from subscriptions.application.contact.contact import get_address_info


@login_required
def user_courses(request):
    """Renders a user dashboard with all the user's registered courses."""
    student_courses = get_user_courses(request.user)
    context = {
        'student_courses': student_courses,
        'address': get_address_info
    }
    return render(request, 'student/user_courses.html', context)
