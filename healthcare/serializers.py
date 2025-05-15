from rest_framework import serializers
from .models import Patient, Doctor, PatientDoctorMapping
from django.contrib.auth.models import User

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['id', 'name', 'date_of_birth', 'gender', 'address', 'phone_number', 
                  'medical_history', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['id', 'name', 'specialization', 'license_number', 
                  'experience_years', 'phone_number', 'email', 
                  'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)


class PatientDoctorMappingSerializer(serializers.ModelSerializer):
    patient_name = serializers.CharField(source='patient.name', read_only=True)
    doctor_name = serializers.CharField(source='doctor.name', read_only=True)

    class Meta:
        model = PatientDoctorMapping
        fields = ['id', 'patient', 'doctor', 'patient_name', 'doctor_name', 
                  'assigned_date', 'notes', 'active']
        read_only_fields = ['id', 'assigned_date']


class PatientWithDoctorsSerializer(PatientSerializer):
    doctors = serializers.SerializerMethodField()

    class Meta(PatientSerializer.Meta):
        fields = PatientSerializer.Meta.fields + ['doctors']

    def get_doctors(self, obj):
        mappings = PatientDoctorMapping.objects.filter(patient=obj, active=True)
        doctors = [mapping.doctor for mapping in mappings]
        return DoctorSerializer(doctors, many=True).data


class DoctorWithPatientsSerializer(DoctorSerializer):
    patients = serializers.SerializerMethodField()

    class Meta(DoctorSerializer.Meta):
        fields = DoctorSerializer.Meta.fields + ['patients']

    def get_patients(self, obj):
        mappings = PatientDoctorMapping.objects.filter(doctor=obj, active=True)
        patients = [mapping.patient for mapping in mappings]
        return PatientSerializer(patients, many=True).data
