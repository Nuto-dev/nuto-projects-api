from django.urls import path, include
from rest_framework.routers import DefaultRouter

from workspace.relations.views import WorkRelationsViewSet

router = DefaultRouter()
router.register('', WorkRelationsViewSet, basename='relations')

urlpatterns = [
    path('', include(router.urls)),
]