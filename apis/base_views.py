from rest_framework.views import APIView
from rest_framework.response import Response


class BaseAPIView(APIView):

    def get_serializer_context(self):
        return {
            'request': self.request,
            'view': self
        }

    def get_serializer(self, *args, **kwargs):
        kwargs['context'] = self.get_serializer_context()
        return self.serializer_class(*args, **kwargs)

    def get_error_message(self, serializer):
        return serializer.errors

    def set_context(self, *args, **kwargs):
        context = {
            'data': kwargs.get('serializer').data
        }
        return context

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            context = self.set_context(serializer=serializer)
            return Response(context)

        return Response({'message': self.get_error_message(serializer)})
