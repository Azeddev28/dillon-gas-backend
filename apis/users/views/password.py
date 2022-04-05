from rest_framework.response import Response
from rest_framework.exceptions import ParseError

from apis.base_views import BaseAPIView
from apis.users.serializers.password import ResetPasswordSerializedr


class ResetPasswordAPIView(BaseAPIView):
    serializer_class = ResetPasswordSerializedr
    success_message = "Password updated successfully"

    def validate_session(self):
        if (not self.request.session.get('email')
            or not self.request.session.get('verification_code')):
            raise ParseError(detail='Invalid Request!')

    def clear_session_data(self):
        del self.request.session['email']
        del self.request.session['verification_code']

    def save_password(self, validated_data):
        user = validated_data.get('user')
        password = validated_data.get('new_password')
        user.set_password(password)
        user.save()

    def post(self, request, *args, **kwargs):
        self.validate_session()
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            return Response(self.get_error_message(serializer))

        self.clear_session_data()
        self.save_password(serializer.validated_data)
        return Response({
            "message": self.success_message,
        })
