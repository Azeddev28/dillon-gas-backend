from django.contrib.auth import get_user_model
from django.utils.decorators import method_decorator

from rest_framework.response import Response

from apis.base_decorators import catch_request_exception
from apis.users.mixins.verification import EmailVerificationMixin
from apis.base_views import BaseAPIView
from apis.users.utils.messages import EMAIL_SENT_MESSAGE, EMAIL_VERIFICATION_MESSAGE

User = get_user_model()


@method_decorator(catch_request_exception, name='post')
class ResendEmailAPIView(BaseAPIView, EmailVerificationMixin):
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            return Response(self.get_error_message(serializer))

        user = serializer.validated_data.get('user')
        self.initiate_user_verification(user.email)
        return Response({"message": EMAIL_SENT_MESSAGE})


@method_decorator(catch_request_exception, name='post')
class EmailVerificationAPIView(BaseAPIView):
    """View to verify user email against generated code"""

    def clear_session_data(self):
        del self.request.session['email']
        del self.request.session['verification_code']

    def change_user_status(self, user):
        user.is_active = True
        user.save()

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            return Response(self.get_error_message(serializer))

        user = serializer.valid_data.get('user')
        self.clear_session_data()
        self.change_user_status(user)
        return Response({'message': EMAIL_VERIFICATION_MESSAGE})
