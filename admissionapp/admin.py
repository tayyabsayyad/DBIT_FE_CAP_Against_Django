from django.contrib import admin
from django.contrib import admin
from .models import FirstYearAdmission
from django.contrib import admin
from .models import SecondYearAdmission


@admin.register(FirstYearAdmission)
class FirstYearAdmissionAdmin(admin.ModelAdmin):
    list_display = (
        'full_name',
        'student_email',
        'student_cell_no',
        'father_cell_no',
        'dob_day',
        'dob_month',
        'dob_year',
        'place_of_birth',
        'nationality',
        'mht_cet_percentile',
        'state_merit_no',
        'application_id',
        'submitted_at',
    )
    search_fields = ('full_name', 'student_email', 'application_id')
    list_filter = ('nationality', 'submitted_at')



@admin.register(SecondYearAdmission)
class SecondYearAdmissionAdmin(admin.ModelAdmin):
    list_display = (
        'full_name',
        'student_email',
        'student_cell_no',
        'father_cell_no',
        'dob_day',
        'dob_month',
        'dob_year',
        'place_of_birth',
        'nationality',
        'passed_diploma_branch',
        'diploma_passing_percentage',
        'application_id',
        'submitted_at',
    )
    search_fields = ('full_name', 'student_email', 'application_id')
    list_filter = ('passed_diploma_branch', 'nationality', 'submitted_at')

