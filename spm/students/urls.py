from django.urls import path
from .views import (
    display_course_grades,
    decide_resit_exam,
    display_resit_exam_time,
    display_resit_exam_details,
    display_new_letter_grades,
)

app_name = 'students'

urlpatterns = [
    path('grades/', display_course_grades, name='display_course_grades'),
    path('decide_resit/', decide_resit_exam, name='decide_resit_exam'),
    path('resit_exam_time/', display_resit_exam_time, name='display_resit_exam_time'),
    path('resit_exam_details/', display_resit_exam_details, name='display_resit_exam_details'),
    path('new_letter_grades/', display_new_letter_grades, name='display_new_letter_grades'),
]

    # Password reset URLs
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='password_reset.html'), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
]