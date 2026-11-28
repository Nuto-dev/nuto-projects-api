from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from workspace.relations.models import WorkSpaceRelation
from workspace.relations.permissions import WorkRelationPermission
from workspace.relations.serializers import WorkRelationSerializer, WorkRelationCreateSerializer


class WorkRelationsViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticated, WorkRelationPermission]
    model = WorkSpaceRelation
    serializer_class = WorkRelationSerializer

    def get_queryset(self):
        return self.model.objects.filter(member=self.request.user)

    @action(detail=True, methods=['get'])
    def accept(self, request, *args, **kwargs):
        result = self.get_object().accept()
        if result:
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['get'])
    def deny(self, request, *args, **kwargs):
        result = self.get_object().deny()
        if result:
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['post'], serializer_class=WorkRelationCreateSerializer)
    def invite(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        if not WorkSpaceRelation.objects.filter(mwmber=self.request.user, workspace=serializer.validated_data['workspace'], member_status__in=['owner', 'co_owner', 'admin']).exists():
            return Response({'derail': 'workspace owner/admin action need'}, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        return Response(status=status.HTTP_201_CREATED)

    @action(detail=True, methods=['post'])
    def activate(self, request, *args, **kwargs):
        relation = self.get_object()

        if not WorkSpaceRelation.objects.filter(mwmber=self.request.user, workspace=relation.workspace, member_status__in=['owner', 'co_owner', 'admin']).exists():
            return Response({'derail': 'workspace owner/admin action need'}, status=status.HTTP_400_BAD_REQUEST)

        relation.active()
        return Response(status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'])
    def deactivate(self, request, *args, **kwargs):
        relation = self.get_object()

        if not WorkSpaceRelation.objects.filter(mwmber=self.request.user, workspace=relation.workspace, member_status__in=['owner', 'co_owner', 'admin']).exists():
            return Response({'derail': 'workspace owner/admin action need'}, status=status.HTTP_400_BAD_REQUEST)

        relation.deactive()
        return Response(status=status.HTTP_200_OK)