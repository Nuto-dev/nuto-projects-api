from rest_framework import serializers

from workspace.relations.models import WorkSpaceRelation
from workspace.space.models import WorkSpace


class WorkSpaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkSpace
        fields = '__all__'
        read_only_fields = ['owner', 'created_at']

    def create(self, validated_data):
        workspace = super(WorkSpaceSerializer, self).create(validated_data)
        WorkSpaceRelation.objects.create(
            workspace=workspace,
            member=workspace.owner,
            member_status=WorkSpaceRelation.MemberStatusChoices.owner,
            invitation_status=WorkSpaceRelation.InvitationStatus.accepted
        )
        return workspace