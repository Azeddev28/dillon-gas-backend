from django.shortcuts import render


def index(request):
    return render(request, 'email_templates/order_tracking.html', {})