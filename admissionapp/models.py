from django.db import models
from django.contrib.auth.models import User

GENDER_CHOICES = [
    ('Male', 'Male'),
    ('Female', 'Female'),
]
class FirstYearAdmission(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='first_year_application')

    full_name = models.CharField(max_length=255)  # Full name of student
    religion = models.CharField(max_length=100)
    correspondence_address = models.TextField()
    student_cell_no = models.CharField(max_length=15)
    student_email = models.EmailField()
    father_cell_no = models.CharField(max_length=15)
    dob_day = models.PositiveSmallIntegerField()
    dob_month = models.PositiveSmallIntegerField()
    dob_year = models.PositiveSmallIntegerField()
    # convenience property for full DOB as date-field (optional)
    # Combine in form/model clean method

    place_of_birth = models.CharField(max_length=255)  # Place of Birth including District and State in single text
    nationality = models.CharField(max_length=100)

    mht_cet_percentile = models.DecimalField(max_digits=6, decimal_places=2)
    state_merit_no = models.CharField(max_length=50)
    application_id = models.CharField(max_length=50, unique=True)  # Application ID - likely unique

    submitted_at = models.DateTimeField(auto_now_add=True)  # keep track submission time

    def __str__(self):
        return f"{self.full_name} - {self.application_id}"

class SecondYearAdmission(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='second_year_application')

    full_name = models.CharField(max_length=255)
    religion = models.CharField(max_length=100)
    correspondence_address = models.TextField()
    student_cell_no = models.CharField(max_length=15)
    student_email = models.EmailField()
    father_cell_no = models.CharField(max_length=15)

    dob_day = models.PositiveSmallIntegerField()
    dob_month = models.PositiveSmallIntegerField()
    dob_year = models.PositiveSmallIntegerField()

    place_of_birth = models.CharField(max_length=255)
    nationality = models.CharField(max_length=100)

    passed_diploma_branch = models.CharField(max_length=255, blank=True, null=True)
    diploma_passing_percentage = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    application_id = models.CharField(max_length=50, unique=True)

    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.application_id}"