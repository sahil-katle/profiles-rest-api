from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class HelloApiView(APIView):
    """ Test API view
    """ 
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
    
