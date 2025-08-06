from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import FirstYearAdmission, SecondYearAdmission

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class FirstYearAdmissionForm(forms.ModelForm):
    class Meta:
        model = FirstYearAdmission
        fields = [
            'full_name',
            'religion',
            'correspondence_address',
            'student_cell_no',
            'student_email',
            'father_cell_no',
            'dob_day',
            'dob_month',
            'dob_year',
            'place_of_birth',
            'nationality',
            'mht_cet_percentile',
            'state_merit_no',
            'application_id',
        ]
        widgets = {
            'correspondence_address': forms.Textarea(attrs={'rows': 3}),
        }


class SecondYearAdmissionForm(forms.ModelForm):
    class Meta:
        model = SecondYearAdmission
        fields = [
            'full_name',
            'religion',
            'correspondence_address',
            'student_cell_no',
            'student_email',
            'father_cell_no',
            'dob_day',
            'dob_month',
            'dob_year',
            'place_of_birth',
            'nationality',
            'passed_diploma_branch',
            'diploma_passing_percentage',
            'application_id',
        ]
        widgets = {
            'correspondence_address': forms.Textarea(attrs={'rows': 3}),
        }
