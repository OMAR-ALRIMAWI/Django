from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Email is required")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, blank=True)  # First name field
    last_name = models.CharField(max_length=30, blank=True)   # Last name field
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

 

class Course(models.Model):
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="courses")
    course_code = models.CharField(max_length=10)
    course_name = models.CharField(max_length=100)
    grade = models.IntegerField()  # Original grade
    letter_grade = models.CharField(max_length=2, blank=True)  # Letter grade (e.g., AA, BB)
    resit = models.BooleanField(default=False)  # Whether the student is attending the resit
    resit_exam_time = models.DateTimeField(null=True, blank=True)
    resit_exam_details = models.TextField(blank=True)
    new_grade = models.IntegerField(null=True, blank=True)  # Updated grade after resit
    new_letter_grade = models.CharField(max_length=2, blank=True)  # Updated letter grade
    attendance_status = models.CharField(
        max_length=10,
        choices=[('Mandatory', 'Mandatory'), ('Optional', 'Optional'), ('Declined', 'Declined')],
        default='Declined'
    )

    def result(self):
        """Determine if the student passed or failed."""
        grade_to_check = self.new_grade if self.new_grade is not None else self.grade
        return "Passed" if grade_to_check >= 50 else "Failed"

    def __str__(self):
        return f"{self.course_code} - {self.course_name}"