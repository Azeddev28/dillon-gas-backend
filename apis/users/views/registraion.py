from django.utils.decorators import method_decorator

from rest_framework.response import Response

from apis.base_decorators import catch_request_exception
from apis.base_views import BaseAPIView
from apis.users.mixins.verification import EmailVerificationMixin
from apis.users.utils.messages import USER_REGISTRATION_SUCCESS_MESSAGE
from apis.users.serializers.registration import RegisterSerializer


@method_decorator(catch_request_exception, name='post')
class RegisterUserAPIView(BaseAPIView, EmailVerificationMixin):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            return Response(self.get_error_message(serializer))

        serializer.save()
        user_data = serializer.data
        self.initiate_user_verification(user_data.get('email'))
        return Response({
            "message": USER_REGISTRATION_SUCCESS_MESSAGE,
            "data": user_data
        })
