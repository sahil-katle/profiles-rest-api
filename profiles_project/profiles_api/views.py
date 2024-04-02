from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers

# Create your views here.
class HelloApiView(APIView):
    """ Test API view
    """ 
    serializer_class = serializers.HelloSerializer
    def get(self, request, format=None):
        """Returns list of APIView features
        """  
        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'IS similar to traditional django view',
            'Give control over app logic',
            'Is mapped manually to urls'
        ]         

        return Response({'message':'Hello', 'an_apiview': an_apiview})
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f"Hello {name}."
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST )
    
    def patch(self, request, pk=None):
        return Response({'method':'patch'})
    
    def put(self, request, pk=None):
        return Response({'method':'put'})
    
    def delete(self, request, pk=None):
        return Response({'method':'delete'})
    
