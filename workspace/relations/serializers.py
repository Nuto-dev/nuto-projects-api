from rest_framework import serializers

from workspace.relations.models import WorkSpaceRelation


class WorkRelationSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkSpaceRelation
        fields = '__all__'
        read_only_fields = fields

class WorkRelationCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkSpaceRelation
        exclude = ['is_active', 'joined_at', 'invitation_status']