from django.urls import path
from rest_framework.routers import DefaultRouter

from accounts.users.views import UserViewSet

router = DefaultRouter()
router.register('', UserViewSet)

urlpatterns = [
    path('', router.urls)
]