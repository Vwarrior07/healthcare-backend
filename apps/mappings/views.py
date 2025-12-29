from rest_framework import viewsets, permissions
from rest_framework.exceptions import PermissionDenied
from .models import PatientDoctor
from .serializers import PatientDoctorSerializer
from apps.patients.models import Patient

class PatientDoctorViewSet(viewsets.ModelViewSet):
    serializer_class = PatientDoctorSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        patient_id = self.kwargs.get('patient_id')
        queryset = PatientDoctor.objects.filter(
            patient__user=self.request.user
        )

        if patient_id:
            queryset = queryset.filter(patient_id=patient_id)

        return queryset

    def perform_create(self, serializer):
        patient = serializer.validated_data['patient']
        if patient.user != self.request.user:
            raise PermissionDenied("You do not own this patient.")
        serializer.save()
