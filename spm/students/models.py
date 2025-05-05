from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    username = None  # Remove the username field
    email = models.EmailField(unique=True)  # Use email as the unique identifier
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    role = models.CharField(max_length=20, choices=[('student', 'Student'), ('instructor', 'Instructor'), ('secretary', 'Secretary')], default='student')  # Optional: Add roles

    USERNAME_FIELD = 'email'  # Set email as the login field
    REQUIRED_FIELDS = []  # No additional required fields

    def __str__(self):
        return self.email


class Course(models.Model):
    student = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="courses")
    course_code = models.CharField(max_length=10)
    course_name = models.CharField(max_length=100)
    instructor_name = models.CharField(max_length=100)
    grade = models.CharField(max_length=2, blank=True, null=True)  # Example: "AA", "BB", etc.
    resit = models.BooleanField(default=False)
    attendance_status = models.CharField(max_length=20, blank=True, null=True)  # Example: "Mandatory", "Optional", etc.

    def __str__(self):
        return f"{self.course_code} - {self.course_name}"