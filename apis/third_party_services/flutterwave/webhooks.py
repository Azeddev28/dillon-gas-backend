import json
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.views import View
from django.utils.decorators import method_decorator

from apis.wallets.models import VirtualAccountPayment


@method_decorator(csrf_exempt, name='dispatch')
class VirtualAccountPaymentWebhook(View):
    def post(self, request):
        try:
            body_unicode = request.body.decode('utf-8')
            payment = json.loads(body_unicode)
            VirtualAccountPayment.objects.create(**payment)
            return HttpResponse('Payment Recieved')

        except Exception as e:
            return HttpResponse(e)
