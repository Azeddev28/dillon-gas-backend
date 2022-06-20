"""dillon_gas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.utils.html import format_html
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from apis.users import urls as user_urls
from apis.inventory import urls as inventory_urls
from apis.stations import urls as station_urls
from apis.ratings import urls as rating_urls
from apis.orders import urls as order_urls
from apis.transactions import urls as transaction_urls
from apis.wallets import urls as wallet_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include(user_urls)),
    path('inventory/', include(inventory_urls)),
    path('stations/', include(station_urls)),
    path('ratings/', include(rating_urls)),
    path('orders/', include(order_urls)),
    path('transactions/', include(transaction_urls)),
    path('wallets/', include(wallet_urls)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


site_header = 'Dillon Gas'
admin.site.site_header = format_html(site_header)
