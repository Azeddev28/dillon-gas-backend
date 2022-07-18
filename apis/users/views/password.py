from rest_framework.response import Response

from apis.base_views import BaseAPIView
from apis.users.serializers.password import ResetPasswordSerializedr


class ResetPasswordAPIView(BaseAPIView):
    serializer_class = ResetPasswordSerializedr
    success_message = "Password updated successfully"

    def save_password(self, validated_data):
        user = validated_data.get('user')
        password = validated_data.get('new_password')
        user.set_password(password)
        user.save()

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        self.save_password(serializer.validated_data)
        return Response({
            "message": self.success_message,
        })
