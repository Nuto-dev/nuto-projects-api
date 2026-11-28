from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated
from workspace.space.models import WorkSpace
from workspace.space.permissions import WorkSpacePermission
from workspace.space.serializers import WorkSpaceSerializer


class WorkSpaceViewSet(
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):
    permission_classes = [IsAuthenticated, WorkSpacePermission]
    model = WorkSpace
    serializer_class = WorkSpaceSerializer

    def get_queryset(self):
        return self.model.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)