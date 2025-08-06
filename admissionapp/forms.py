from django import forms
from .models import FirstYearAdmission, SecondYearAdmission

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
