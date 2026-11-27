from rest_framework import viewsets, mixins, status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from accounts.users.models import User
from accounts.users.permissions import UserViewSetPermission
from accounts.users.serializers import UserSerializer, LoginSerializer


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

    @action(detail=False, methods=['post'], permission_classes=[AllowAny], serializer_class=LoginSerializer)
    def login(self, request, *args, **kwargs):
        serial = self.get_serializer(data=request.data)
        serial.is_valid(raise_exception=True)

        email = serial.data.get('email')
        password = serial.data.get('password')

        try:
            user = self.get_queryset().get(email=email)
            verification = user.check_password(password)

            if verification:
                refresh = RefreshToken.for_user(user)
                return Response({
                    'access': str(refresh.access_token),
                    'refresh': str(refresh),
                }, status=status.HTTP_200_OK)

        except self.model.DoesNotExist:
            pass
        return Response(status=status.HTTP_400_BAD_REQUEST)