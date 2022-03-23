from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.views import Response

# Create your views here.

class HelloAPIView(APIView):
    def get(self, request, format=None):
        an_apiview = [
            "Hello Wordl"
        ]
        return Response({'message': 'hello', 'an_apiview': an_apiview})