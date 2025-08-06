from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.urls import path, include

app_name = 'admissionapp'

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),

    path('', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('first-year/apply/', views.first_year_admission_view, name='first_year_admission'),
    path('first-year/details/', views.first_year_admission_detail, name='first_year_admission_detail'),

    path('second-year/apply/', views.second_year_admission_view, name='second_year_admission'),
    path('second-year/details/', views.second_year_admission_detail, name='second_year_admission_detail'),


    path('application/view/', views.application_view, name='application_view'),

    path('application/edit/', views.application_edit, name='application_edit'),

    path('application/download_pdf/', views.download_application_pdf, name='download_application_pdf'),

    path('register/', views.register, name='register'),

    path('application/', views.application_form, name='application_form'),

    path('forgot-password/', auth_views.PasswordResetView.as_view(
        template_name='forgot_password.html'), name='forgot_password'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(
        template_name='password_reset_complete.html'), name='password_reset_complete'),

    # Dashboard (home for logged in user)

    path('dashboard/', views.dashboard, name='dashboard'),

    # In urls.py
    path('admin/application/<int:pk>/', views.application_admin_view, name='application_admin_view'),
    path('admin/application/<int:pk>/download/', views.download_application_pdf_by_id,
         name='download_application_pdf_by_id'),
    path('applications/all/', views.application_list, name='application_list'),
    path('applications/<int:pk>/', views.application_admin_view, name='application_admin_view'),
    path('applications/<int:pk>/pdf/', views.download_application_pdf_by_id, name='download_application_pdf_by_id'),
    path('applications/export_excel/', views.export_applications_excel, name='export_applications_excel'),
]
