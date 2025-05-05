from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.views.generic import FormView
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from .models import CustomUser, Course
from .forms import EmailAuthenticationForm


class StudentLoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

class EmailAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'autofocus': True}))


class StudentLoginView(FormView):
    template_name = 'student-login.html'
    form_class = EmailAuthenticationForm
    success_url = reverse_lazy('students:student_home')

    def form_valid(self, form):
        email = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(self.request, username=email, password=password)
        if user:
            login(self.request, user)
            return super().form_valid(form)
        form.add_error(None, "Invalid email or password")
        return self.form_invalid(form)


def landing_page(request):
    return render(request, 'exam-redo.html')  # Updated template name

@login_required
def student_home(request):
    return render(request, 'index.html', {'user': request.user})

@login_required
def profile_page(request):
    return render(request, 'profilepage.html', {'user': request.user})

@login_required
def display_course_grades(request):
    courses = Course.objects.filter(student=request.user)
    return render(request, 'course-grades.html', {'courses': courses})

@login_required
def decide_resit_exam(request):
    courses = Course.objects.filter(student=request.user)
    if request.method == "POST":
        course_id = request.POST.get('course_id')
        course = get_object_or_404(Course, id=course_id, student=request.user)
        course.resit = True
        course.attendance_status = "Mandatory"
        course.save()
        return redirect('students:decide_resit_exam')
    return render(request, 'attend-reset.html', {'courses': courses})

@login_required
def display_resit_exam_time(request):
    courses = Course.objects.filter(student=request.user, resit=True)
    return render(request, 'reset-exam-schedual.html', {'courses': courses})

@login_required
def display_resit_exam_details(request):
    courses = Course.objects.filter(student=request.user, resit=True)
    return render(request, 'reset-exam-details.html', {'courses': courses})

@login_required
def display_new_letter_grades(request):
    courses = Course.objects.filter(student=request.user)
    return render(request, 'course-grades.html', {'courses': courses})


# ✅ Fixed: moved outside, properly defined
def exam_redo_view(request):
    return render(request, 'exam_redo.html')