from django.utils.decorators import method_decorator
from django.contrib.auth import logout

from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView

from apis.base_decorators import catch_request_exception
from apis.users.authentication.token_auth import DGTokenAuthentication
from apis.users.serializers.authentication import DGAuthTokenSerializer
from apis.users.utils.messages import INVALID_REQUEST_MESSAGE, LOGOUT_MESSAGE


class DGTokenObtainView(ObtainAuthToken):
    serializer_class = DGAuthTokenSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token = Token.objects.filter(user=user).delete()
        token = Token.objects.create(user=user)
        return Response({'token': token.key})


@method_decorator(catch_request_exception, name='post')
class LogoutView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [DGTokenAuthentication]
    success_message = LOGOUT_MESSAGE

    def post(self, request):
        if Token.objects.filter(user=request.user):
            request.user.auth_token.delete()
            logout(request)
            return Response({'message': self.success_message})

        return Response({'message': INVALID_REQUEST_MESSAGE})
