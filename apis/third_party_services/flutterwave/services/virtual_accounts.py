
import requests
import json
from django.conf import settings


class VirtualAccountService:
    TRANSACTION_REFERENCE = 'VA12'
    HTTP_METHOD = 'POST'

    def __init__(self):
        self.target_url = f'{settings.FLUTTERWAVE_BASE_URL}/virtual-account-numbers'

    def get_request_body(self):
        request_body = {
            'email': settings.FLUTTERWAVE_ADMIN_EMAIL,
            'is_permanent': True,
            'bvn': settings.BVN_ACCOUNT_NUMBER,
            'tx_ref': self.TRANSACTION_REFERENCE,
            'phonenumber': settings.FLUTTERWAVE_ADMIN_PHONE_NUMBER,
            'firstname': settings.FLUTTERWAVE_ADMIN_FIRST_NAME,
            'lastname': settings.FLUTTERWAVE_ADMIN_LAST_NAME,
            'narration': settings.FLUTTERWAVE_VIRTUAL_ACCOUNT_NARRATION
        }
        request_body = json.dumps(request_body)
        return request_body

    def get_request_headers(self):
        request_headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {settings.FLUTTERWAVE_SECRET_KEY}'
        }
        return request_headers

    def fetch(self, *args, **kwargs):
        response = requests.post(
            url=self.target_url,
            headers=self.get_request_headers(),
            data=self.get_request_body()
        )
        return response
