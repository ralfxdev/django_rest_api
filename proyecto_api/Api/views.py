from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.views import Response
from rest_framework import status
from Api import serializers

# Create your views here.

class HelloAPIView(APIView):
    def get(self, request, format=None):
        an_apiview = [
            "Hello Wordl"
        ]
        return Response({'message': 'hello', 'an_apiview': an_apiview})

    serializers_class = serializers.HelloSerializer

    #Creamos el método POST

    def post(self, request):
        serializer = self.serializers_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST,
            )

    def put(self, request, pk=None):
        return Response({'method': 'PUT'})
    
    def delete(self, request, pk=None):
        return Response({'method': 'DELETE'})
    
    def patch(self, request, pk=None):
        return Response({'method': 'PATCH'})