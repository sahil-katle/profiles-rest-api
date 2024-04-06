from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from profiles_api import serializers
from profiles_api import models
from profiles_api import permissions

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

class HelloViewSet(viewsets.ViewSet):
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        a_viewset = 'Provides more functionality with less code!'

        return Response({'message': 'Hello',
                         'a_viewset': a_viewset})
    
    def create(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            msg = f'Hello {name}'
            return Response({'msg':msg})
        else:
            return Response(serializer.errors, 
                            status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self, request, pk=None):
        return Response({'method':'GET'})
    
    def update(self, request, pk=None):
        return Response({'method':'PUT'})
    
    def partial_update(self, request, pk=None):
        return Response({'method':'partial_update'})
    
    def destroy(self, request, pk=None):
        return Response({'method':'destroy'})
    
class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating of profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset= models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email')

class UserLoginAPiView(ObtainAuthToken):
    """Handle creating user authentication tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES    
