from rest_framework import viewsets, permissions
from .models import Patient
from .serializers import PatientSerializer

class PatientViewSet(viewsets.ModelViewSet):
    serializer_class = PatientSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Only return patients created by this user
        return Patient.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Attach logged-in user automatically
        serializer.save(user=self.request.user)
