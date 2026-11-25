from rest_framework import serializers
from accounts.users.models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False, max_length=128)

    class Meta:
        model = User
        exclude = ['created_at', 'id']

    def create(self, validated_data):
        password = validated_data.pop('password', None)

        if not password:
            raise serializers.ValidationError('password is required')

        user = User(**validated_data)
        user.set_password(password)
        user.save()

        return user

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)

        if password:
            instance.set_password(password)

        return super(UserSerializer, self).update(instance, validated_data)