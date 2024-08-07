from django.contrib.auth import get_user_model

from rest_framework.generics import DestroyAPIView
from rest_framework.permissions import IsAuthenticated

User = get_user_model()


class UserDeletionAPIView(DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()

    def get_object(self):
        user = self.request.user
        return user
