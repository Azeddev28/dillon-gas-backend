from rest_framework.response import Response

from apis.base_views import BaseAPIView
from apis.users.mixins.verification import SaveSessionMixin
from apis.users.utils.messages import USER_REGISTRATION_SUCCESS_MESSAGE
from apis.users.serializers.registration import RegisterSerializer


class RegisterUserAPIView(BaseAPIView, SaveSessionMixin):
    serializer_class = RegisterSerializer
    success_message = USER_REGISTRATION_SUCCESS_MESSAGE

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save()
        user_data = serializer.data
        verification_code = user_data.pop('verification_code')
        self.save_session_params(user_data.get('email'), verification_code)
        return Response({
            "message": self.success_message,
            "data": user_data
        })
