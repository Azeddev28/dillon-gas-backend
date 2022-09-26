from django.contrib.auth import get_user_model

from rest_framework.generics import DestroyAPIView
from rest_framework.permissions import IsAuthenticated

User = get_user_model()


class UserDeletionAPIView(DestroyAPIView):
    lookup_field = 'uuid'
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
