from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken

from django.contrib.auth import logout
from django.contrib.auth import authenticate, login


class LoginViewSet(viewsets.ViewSet):

    serializer_class = AuthTokenSerializer

    def create(self,request):
        """Use the ObtainAuthToken APIView to validate and create a token"""

        return ObtainAuthToken().post(request)
