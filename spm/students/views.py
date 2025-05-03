from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.views.generic import FormView, CreateView
from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from .models import CustomUser
from .forms import EmailAuthenticationForm

class StudentLoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

class EmailAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'autofocus': True}))

class StudentLoginView(FormView):
    template_name = 'studentlogin.html'
    form_class = EmailAuthenticationForm
    success_url = reverse_lazy('students:student_home')

    def form_valid(self, form):
        email = form.cleaned_data['username']  # Email is passed as 'username' in the form
        password = form.cleaned_data['password']

        user = authenticate(self.request, username=email, password=password)  # Use email for authentication
        if user:
            login(self.request, user)
            return super().form_valid(form)

        form.add_error(None, "Invalid email or password")
        return self.form_invalid(form)
        
class InstructorLoginView(FormView):
    template_name = 'login_instructor.html'
    form_class = EmailAuthenticationForm
    success_url = reverse_lazy('students:instructor_home')

    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)
        return super().form_valid(form)

class SecretaryLoginView(FormView):
    template_name = 'login_secretary.html'
    form_class = EmailAuthenticationForm
    success_url = reverse_lazy('students:secretary_home')

    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)
        return super().form_valid(form)

def landing_page(request):
    return render(request, 'landing.html')

def student_home(request):
 return render(request, 'profilepage.html', {'user': request.user})

@login_required
def profile_page(request):
    return render(request, 'profilepage.html', {
        'user': request.user,
    })

@login_required
def display_course_grades(request):
    """Display the student's courses with grades and results."""
    courses = Course.objects.filter(student=request.user)
    return render(request, 'display_course_grades.html', {'courses': courses})

    @login_required
def decide_resit_exam(request):
    """Allow the student to confirm attendance for resit exams."""
    courses = Course.objects.filter(student=request.user)
    if request.method == "POST":
        course_id = request.POST.get('course_id')
        course = get_object_or_404(Course, id=course_id, student=request.user)
        course.resit = True
        course.attendance_status = "Mandatory"  # Example: Set status to Mandatory
        course.save()
        return redirect('students:decide_resit_exam')
    return render(request, 'decide_resit_exam.html', {'courses': courses})

    @login_required
def display_resit_exam_time(request):
    """Display the resit exam schedule."""
    courses = Course.objects.filter(student=request.user, resit=True)
    return render(request, 'display_resit_exam_time.html', {'courses': courses})

    @login_required
def display_resit_exam_details(request):
    """Display detailed instructions for resit exams."""
    courses = Course.objects.filter(student=request.user, resit=True)
    return render(request, 'display_resit_exam_details.html', {'courses': courses})
    @login_required
def display_new_letter_grades(request):
    """Display updated grades and letter grades after resit exams."""
    courses = Course.objects.filter(student=request.user)
    return render(request, 'display_new_letter_grades.html', {'courses': courses})