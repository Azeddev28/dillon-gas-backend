from apis.users.views.authentication import DGTokenObtainView, LogoutView
from apis.users.views.password import ResetPasswordAPIView
from apis.users.views.registraion import RegisterUserAPIView
from apis.users.views.user_details import CustomerDetailsRetrieveAPIView
from apis.users.views.verification import EmailVerificationAPIView, ResendEmailAPIView
from apis.users.views.registraion import RegisterUserAPIView


auth_token_view = DGTokenObtainView.as_view()
logout_view = LogoutView.as_view()
register_view = RegisterUserAPIView.as_view()
resend_email_view = ResendEmailAPIView.as_view()
email_verification_view = EmailVerificationAPIView.as_view()
reset_password_view = ResetPasswordAPIView.as_view()
customer_details_view = CustomerDetailsRetrieveAPIView.as_view()
