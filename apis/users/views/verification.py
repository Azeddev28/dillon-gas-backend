from django.contrib.auth import get_user_model
from django.utils.decorators import method_decorator

from rest_framework.response import Response
from rest_framework.exceptions import ParseError

from apis.base_decorators import catch_request_exception
from apis.base_views import BaseAPIView
from apis.services.email_service import EmailService
from apis.users.serializers.verification import EmailVerificationSerializer, ResendEmailSerializer
from apis.users.utils.messages import EMAIL_SENT_MESSAGE, EMAIL_VERIFICATION_MESSAGE
from apis.users.views.registraion import RegisterUserAPIView

User = get_user_model()


# @method_decorator(catch_request_exception, name='post')
class ResendEmailAPIView(RegisterUserAPIView):
    serializer_class = ResendEmailSerializer
    success_message = EMAIL_SENT_MESSAGE

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
            # return Response(self.get_error_message(serializer))

        user = serializer.validated_data.get('user')
        verification_code = serializer.validated_data.pop('verification_code')
        self.save_session_params(user.email, verification_code)
        email_service = EmailService(
            'Email Verification',
            [user.email,],
            'email_templates/otp_email.html',
            {
                'verification_code': verification_code
            }
        )
        email_service.start()
        return Response({
            "message": self.success_message,
        })


# @method_decorator(catch_request_exception, name='post')
class EmailVerificationAPIView(BaseAPIView):
    """View to verify user email against generated code"""
    serializer_class = EmailVerificationSerializer
    success_message = EMAIL_VERIFICATION_MESSAGE

    def validate_session(self):
        if (not self.request.session.get('email')
                or not self.request.session.get('verification_code')):
            raise ParseError(detail='Invalid Request!')

    def clear_session_data(self):
        del self.request.session['email']
        del self.request.session['verification_code']

    def change_user_status(self, user):
        user.is_active = True
        user.save()

    def post(self, request, *args, **kwargs):
        self.validate_session()
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data.get('user')
        self.clear_session_data()
        self.change_user_status(user)
        return Response({'message': self.success_message})
