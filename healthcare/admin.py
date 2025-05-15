from django.contrib import admin
from .models import Patient, Doctor, PatientDoctorMapping

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('name', 'gender', 'date_of_birth', 'phone_number', 'created_at')
    search_fields = ('name', 'phone_number')
    list_filter = ('gender', 'created_at')


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'specialization', 'license_number', 'experience_years', 'email')
    search_fields = ('name', 'specialization', 'license_number')
    list_filter = ('specialization', 'experience_years')


@admin.register(PatientDoctorMapping)
class PatientDoctorMappingAdmin(admin.ModelAdmin):
    list_display = ('patient', 'doctor', 'assigned_date', 'active')
    list_filter = ('active', 'assigned_date')
    search_fields = ('patient__name', 'doctor__name', 'notes')
