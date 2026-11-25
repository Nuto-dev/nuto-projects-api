from rest_framework import viewsets, mixins
from accounts.users.models import User
from accounts.users.permissions import UserViewSetPermission
from accounts.users.serializers import UserSerializer


class UserViewSet(
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):
    permission_classes = [UserViewSetPermission]
    queryset = User.objects.all()
    model = User
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user
