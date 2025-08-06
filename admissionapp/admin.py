from django.contrib import admin

from .models import SecondYearAdmission
@admin.register(SecondYearAdmission)
class SecondYearAdmissionAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'application_id', 'submitted_at')