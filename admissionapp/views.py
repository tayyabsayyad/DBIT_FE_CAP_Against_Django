from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from django.template.loader import render_to_string
from weasyprint import HTML
from django.http import HttpResponse
import openpyxl
from openpyxl.utils import get_column_letter
from io import BytesIO
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import FirstYearAdmissionForm, SecondYearAdmissionForm
from .models import FirstYearAdmission, SecondYearAdmission


@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

@login_required
def first_year_admission_view(request):
    try:
        existing_app = request.user.first_year_application
        return redirect('admissionapp:first_year_admission_detail')
    except FirstYearAdmission.DoesNotExist:
        existing_app = None

    if request.method == 'POST':
        form = FirstYearAdmissionForm(request.POST)
        if form.is_valid():
            admission = form.save(commit=False)
            admission.user = request.user
            admission.save()
            return redirect('admissionapp:first_year_admission_detail')
    else:
        form = FirstYearAdmissionForm()

    return render(request, 'admissionapp/first_year_form.html', {'form': form})


@login_required
def second_year_admission_view(request):
    try:
        existing_app = request.user.second_year_application
        return redirect('admissionapp:second_year_admission_detail')
    except SecondYearAdmission.DoesNotExist:
        existing_app = None

    if request.method == 'POST':
        form = SecondYearAdmissionForm(request.POST)
        if form.is_valid():
            admission = form.save(commit=False)
            admission.user = request.user
            admission.save()
            return redirect('admissionapp:second_year_admission_detail')
    else:
        form = SecondYearAdmissionForm()

    return render(request, 'admissionapp/second_year_form.html', {'form': form})

@login_required
def first_year_admission_detail(request):
    try:
        app = request.user.first_year_application
    except FirstYearAdmission.DoesNotExist:
        return redirect('admissionapp:first_year_admission')

    return render(request, 'first_year_detail.html', {'app': app})

@login_required
def second_year_admission_detail(request):
    try:
        app = request.user.second_year_application
    except SecondYearAdmission.DoesNotExist:
        return redirect('admissionapp:second_year_admission')

    return render(request, 'second_year_detail.html', {'app': app})





@login_required
def application_form(request):
    # Only allow single submission per user
    try:
        existing = request.user.cap_application
        return redirect('admissionapp:application_view')
    except CapApplication.DoesNotExist:
        existing_app = None

    if request.method == "POST":
        form = CapApplicationForm(request.POST)
        if form.is_valid():
            app = form.save(commit=False)
            app.dob = form.cleaned_data['dob']
            app.age = form.cleaned_data['age']
            app.user = request.user
            app.save()
            return redirect('admissionapp:application_view')
    else:
        form = CapApplicationForm()

    return render(request, 'application_form.html', {'form': form})


@login_required
def application_edit(request):
    # Get or 404 the current user's application
    app = get_object_or_404(CapApplication, user=request.user)

    if request.method == 'POST':
        form = CapApplicationForm(request.POST, instance=app)
        if form.is_valid():
            app = form.save(commit=False)
            # Handle DOB fields if present
            if hasattr(form, 'cleaned_data'):
                if 'dob' in form.cleaned_data:
                    app.dob = form.cleaned_data['dob']
                if 'age' in form.cleaned_data:
                    app.age = form.cleaned_data['age']
            app.save()
            return redirect('application_view')
    else:
        # Prepopulate DOB fields if using split day/month/year in your form
        initial = {}
        if app.dob:
            initial = {
                'dob_day': app.dob.day,
                'dob_month': app.dob.month,
                'dob_year': app.dob.year
            }
        form = CapApplicationForm(instance=app, initial=initial)

    return render(request, 'application_edit.html', {'form': form, 'edit_mode': True})

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful. You can now log in.")
            return redirect('admissionapp:login')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

def forgot_password(request):
    return render(request, 'forgot_password.html')

@login_required
def application_view(request):
    # Show the current user's application (or an error if missing)
    try:
        app = request.user.cap_application
    except CapApplication.DoesNotExist:
        app = None

    return render(request, 'application_view.html', {'app': app})


@login_required
def application_edit(request):
    # Edit the current user's application
    app = get_object_or_404(CapApplication, user=request.user)
    if request.method == 'POST':
        form = CapApplicationForm(request.POST, instance=app)
        if form.is_valid():
            app = form.save(commit=False)
            # If you handle DOB as 3 fields, set dob/age here from cleaned_data
            if 'dob' in form.cleaned_data:
                app.dob = form.cleaned_data['dob']
            if 'age' in form.cleaned_data:
                app.age = form.cleaned_data['age']
            app.save()
            return redirect('application_view')
    else:
        # Set initial data for dob_day/month/year from saved dob:
        initial = {}
        if app.dob:
            initial = {
                'dob_day': app.dob.day,
                'dob_month': app.dob.month,
                'dob_year': app.dob.year
            }
        form = CapApplicationForm(instance=app, initial=initial)
    return render(request, 'application_form.html', {'form': form, 'edit_mode': True})

@login_required
def download_application_pdf(request):
    try:
        app = request.user.cap_application
    except CapApplication.DoesNotExist:
        # Redirect or show error if no application
        return HttpResponse("No application found to generate PDF.", status=404)

    html_string = render_to_string('application_pdf.html', {'app': app})
    html = HTML(string=html_string)
    pdf = html.write_pdf()

    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="CAP_Application_{}.pdf"'.format(request.user.username)
    return response

@staff_member_required  # Only admins and staff can access
def application_list(request):
    applications = CapApplication.objects.all().select_related('user').order_by('-submitted_at')
    return render(request, 'application_list.html', {'applications': applications})

@staff_member_required
def application_admin_view(request, pk):
    app = get_object_or_404(CapApplication, pk=pk)
    return render(request, 'application_view.html', {'app': app, 'admin_mode': True})


@staff_member_required
def download_application_pdf_by_id(request, pk):
    app = get_object_or_404(CapApplication, pk=pk)
    html_string = render_to_string('application_pdf.html', {'app': app})
    html = HTML(string=html_string, base_url=request.build_absolute_uri())
    pdf = html.write_pdf()
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="CAP_Application_{app.pk}.pdf"'
    return response

@staff_member_required
def export_applications_excel(request):
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Applications"

    # Define the headers
    headers = [
        "ID", "Applicant Name", "Email", "Percentile", "Submitted On"
        # add more fields if desired
    ]
    ws.append(headers)

    # Populate rows
    for app in CapApplication.objects.all().order_by('-submitted_at'):
        ws.append([
            app.id,
            f"{app.first_name} {app.surname}",
            app.student_email,
            app.mhtcet_percentile,
            app.submitted_at.strftime('%Y-%m-%d %H:%M'),
            # add more fields as needed
        ])

    # Adjust column widths
    for i, col in enumerate(ws.columns, 1):
        max_length = max(len(str(cell.value)) for cell in col)
        ws.column_dimensions[get_column_letter(i)].width = max_length + 3

    # Create response
    file_stream = BytesIO()
    wb.save(file_stream)
    file_stream.seek(0)  # Go to the beginning of the stream

    response = HttpResponse(
        file_stream.getvalue(),
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response['Content-Disposition'] = 'attachment; filename=all_applications.xlsx'
    return response