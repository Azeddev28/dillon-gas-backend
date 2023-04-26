from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView


class UserFCMTokenRegistrationAPIView(APIView):
    permission_classes = [IsAuthenticated]
    success_message = "FCM Token Added Successfully."

    def post(self, request, *args, **kwargs):
        user = request.user
        user_device = user.device
        fcm_token = request.data.get('fcm_token')
        print(fcm_token)
        user_device.fcm_token = fcm_token
        user_device.save()
        return Response({
            "message": self.success_message,
        })
