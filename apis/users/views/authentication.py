from django.utils.decorators import method_decorator
from django.contrib.auth import logout

from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework.response import Response


from apis.base_decorators import catch_request_exception
from apis.users.utils.messages import INVALID_REQUEST_MESSAGE, LOGOUT_MESSAGE


@method_decorator(catch_request_exception, name='post')
class LogoutView(APIView):
    permission_classes = [IsAuthenticated]
    success_message = LOGOUT_MESSAGE

    def post(self, request):
        if Token.objects.filter(user=request.user):
            request.user.auth_token.delete()
            logout(request)
            return Response({'message': self.success_message})

        return Response({'message': INVALID_REQUEST_MESSAGE})
