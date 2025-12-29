from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import PatientDoctorViewSet

router = DefaultRouter()
router.register(r'', PatientDoctorViewSet, basename='mappings')

urlpatterns = router.urls + [
    path('<int:patient_id>/', PatientDoctorViewSet.as_view({'get': 'list'})),
]
