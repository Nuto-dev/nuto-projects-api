from django.urls import path, include
from rest_framework.routers import DefaultRouter

from workspace.space.views import WorkSpaceViewSet

router = DefaultRouter()
router.register('', WorkSpaceViewSet, basename='workspace')

urlpatterns = [
    path('', include(router.urls)),
]