import json

from rest_framework.views import APIView
from rest_framework.response import Response

from apis.third_party_services.flutterwave.services.virtual_accounts import VirtualAccountService


class VirtualAccountAPIView(APIView):
    def get(self, request, *args, **kwargs):
        virtual_account_service = VirtualAccountService()
        response = virtual_account_service.fetch()
        response_data = json.loads(response.content.decode('utf-8'))
        return Response(data=response_data)
