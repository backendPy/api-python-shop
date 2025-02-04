from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ShirtViewSet, PantsViewSet, ShortsViewSet, CapViewSet

router = DefaultRouter()
router.register(r'shirt', ShirtViewSet)
router.register(r'pants', PantsViewSet)
router.register(r'shorts', ShortsViewSet)
router.register(r'cap', CapViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
