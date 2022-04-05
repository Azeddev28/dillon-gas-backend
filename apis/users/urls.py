from django.urls import path

from apis.users.bindings import (auth_token_view, logout_view,
                                 email_verification_view, register_view,
                                 resend_email_view, reset_password_view,
                                 customer_details_view)


urlpatterns = [
    path('token/', auth_token_view, name='obtain-token'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
    path('verify-account/', email_verification_view, name='account-verification'),
    path('resend-email/', resend_email_view, name='resend-email'),
    path('reset-password/', reset_password_view, name='reset-password'),
    path('user-details/', customer_details_view, name='user-details')
]
