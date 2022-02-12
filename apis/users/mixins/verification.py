from apis.users.utils.registration_utils import generate_verification_code, send_verification_email


class EmailVerificationMixin:
    def save_session_params(self, email, verification_code):
        self.request.session['email'] = email
        self.request.session['verification_code'] = verification_code

    def initiate_user_verification(self, email):
        verification_code = generate_verification_code()
        self.save_session_params(email, verification_code)
        send_verification_email(
            verification_code=verification_code,
            recipient_email=email
        )
