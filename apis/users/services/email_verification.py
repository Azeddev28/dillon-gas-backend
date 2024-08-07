import string
import secrets

from apis.services.email_service import EmailService
from apis.users.utils.constants import EMAIL_BODY, VERIFICATION_CODE


class EmailVerificationService(EmailService):
    def __init__(self, recipient_email, verification_code):
        self.verification_code = verification_code

        subject = VERIFICATION_CODE
        message = self.get_email_body(self.verification_code)
        recipients = [recipient_email]
        super().__init__(subject, message, recipients)

    def get_email_body(self, verification_code):
        return EMAIL_BODY.format(verification_code)

    def get_verification_code(self):
        return self.verification_code

    @staticmethod
    def generate_verification_code():
        return ''.join(secrets.choice(string.digits) for i in range(6))
