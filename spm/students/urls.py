# filepath: c:\Users\owner\Desktop\Django\spm\students\urls.py
from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views
from .views import exam_redo_view
from .views import (
    display_course_grades,
    decide_resit_exam,
    display_resit_exam_time,
    display_resit_exam_details,
    display_new_letter_grades,
    landing_page,
    student_home,
    profile_page,
    StudentLoginView,
)

app_name = 'students'

urlpatterns = [
    path('', landing_page, name='landing_page'),
    path('home/', student_home, name='student_home'),
    path('profile/', profile_page, name='profile_page'),
    path('grades/', display_course_grades, name='display_course_grades'),
    path('decide_resit/', decide_resit_exam, name='decide_resit_exam'),
    path('resit_exam_time/', display_resit_exam_time, name='display_resit_exam_time'),
    path('resit_exam_details/', display_resit_exam_details, name='resit_exam_details'),
    path('new_letter_grades/', display_new_letter_grades, name='new_letter_grades'),
    path('login/', StudentLoginView.as_view(), name='student_login'),

    # Password reset URLs
    path('password_reset/', auth_views.PasswordResetView.as_view(
        template_name='password_reset.html',
        email_template_name='password_reset_email.html',
        success_url=reverse_lazy('students:password_reset_done')
    ), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(
        template_name='password_reset_done.html'
    ), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='password_reset_confirm.html'
    ), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(
        template_name='password_reset_complete.html'
    ), name='password_reset_complete'),

     path('exam-redo/', exam_redo_view, name='exam_redo'),
]