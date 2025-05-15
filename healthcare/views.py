from rest_framework import viewsets, permissions, status, generics
from rest_framework.response import Response
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404

from .models import Patient, Doctor, PatientDoctorMapping
from .serializers import (
    PatientSerializer, 
    DoctorSerializer, 
    PatientDoctorMappingSerializer,
    PatientWithDoctorsSerializer,
    DoctorWithPatientsSerializer
)

class PatientViewSet(viewsets.ModelViewSet):
    serializer_class = PatientSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return Patient.objects.filter(user=self.request.user)
    
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = PatientWithDoctorsSerializer(instance)
        return Response(serializer.data)
    
    @action(detail=True, methods=['get'])
    def doctors(self, request, pk=None):
        patient = self.get_object()
        mappings = PatientDoctorMapping.objects.filter(patient=patient, active=True)
        doctors = [mapping.doctor for mapping in mappings]
        serializer = DoctorSerializer(doctors, many=True)
        return Response(serializer.data)


class DoctorViewSet(viewsets.ModelViewSet):
    serializer_class = DoctorSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return Doctor.objects.filter(user=self.request.user)
    
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = DoctorWithPatientsSerializer(instance)
        return Response(serializer.data)
    
    @action(detail=True, methods=['get'])
    def patients(self, request, pk=None):
        doctor = self.get_object()
        mappings = PatientDoctorMapping.objects.filter(doctor=doctor, active=True)
        patients = [mapping.patient for mapping in mappings]
        serializer = PatientSerializer(patients, many=True)
        return Response(serializer.data)


class PatientDoctorMappingViewSet(viewsets.ModelViewSet):
    serializer_class = PatientDoctorMappingSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        return PatientDoctorMapping.objects.filter(
            patient__user=user
        ) | PatientDoctorMapping.objects.filter(
            doctor__user=user
        )
    
    def perform_create(self, serializer):
        patient = serializer.validated_data['patient']
        doctor = serializer.validated_data['doctor']
        
        # Check if the user has permission to assign this patient and doctor
        if patient.user != self.request.user and doctor.user != self.request.user:
            raise permissions.exceptions.PermissionDenied(
                "You don't have permission to create this mapping."
            )
        
        serializer.save()
