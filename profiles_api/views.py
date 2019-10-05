from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """docstring for HelloApiView."""

    def get(self, request, format=None):
        an_apiview = [
        'Uses HTTP methods as function (get, post, patch, put, delete)',
        'Is similar to traditional Django View',
        'Gives you the most control',
        'Is mapped manually to URLs',
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})

    # def __init__(self, arg):
    #     super(HelloApiView, self).__init__()
    #     self.arg = arg
