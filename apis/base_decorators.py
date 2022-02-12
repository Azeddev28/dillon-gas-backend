from functools import wraps

from rest_framework.response import Response
from rest_framework.status import HTTP_500_INTERNAL_SERVER_ERROR


def catch_request_exception(func):
    @wraps(func)
    def func_wrapper(request, *args, **kwargs):
        try:
            return func(request, *args, **kwargs)
        except Exception as e:
            return Response({
                'message': 'Something went Wrong!'
            }, status=HTTP_500_INTERNAL_SERVER_ERROR)
    return func_wrapper
