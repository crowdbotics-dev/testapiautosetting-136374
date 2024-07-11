from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import Testconnectors136374ViewSet

router = DefaultRouter()
router.register(
    "testconnectors136374", Testconnectors136374ViewSet, basename="testconnectors136374"
)

urlpatterns = [
    path("connectors/", include(router.urls)),
]
