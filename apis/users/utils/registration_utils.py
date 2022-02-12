import string
import secrets

from apis.users.utils.constants import EMAIL_BODY, VERIFICATION_CODE
from apis.services.email_service import EmailService


def generate_verification_code():
    return ''.join(secrets.choice(string.digits) for i in range(6))


def get_email_body(verification_code):
    return EMAIL_BODY.format(verification_code)


def send_verification_email(verification_code, recipient_email):
    email_service = EmailService(
        subject=VERIFICATION_CODE,
        message=get_email_body(verification_code),
        recipients=[recipient_email]
    )
    return email_service.send_email()
