from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import Http404

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView

from customer.serializers import UserAccountSerializer
from customer.models import UserAccount


import logging

logger = logging.getLogger(__name__)


class UserAccountAPI(APIView):
    """
    User account related APIs
    """
    
    def get(self, request, format=None):
    	""" displays all user accouts """
        
        user_accounts = UserAccount.objects.all()
        serializer = UserAccountSerializer(user_accounts, many=True)
        return Response(serializer.data)