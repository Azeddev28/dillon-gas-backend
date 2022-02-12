from rest_framework.authentication import TokenAuthentication


class DGTokenAuthentication(TokenAuthentication):
    keyword = 'Bearer'
