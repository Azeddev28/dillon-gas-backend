

class SaveSessionMixin:
    """Mixin to save session params to request"""
    def save_session_params(self, email, verification_code):
        self.request.session['email'] = email
        self.request.session['verification_code'] = verification_code
