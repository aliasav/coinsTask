from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import Http404

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView

from transactions.serializers import PaymentSerializer
from transactions.models import Payment

import logging

logger = logging.getLogger(__name__)

"""
Example POST data:
{
    "amount":100,
    "from_account": "209f5b13-dc53-48b8-8965-115a8f0538e4",
    "to_account": "a5cea467-1bd6-4c47-9ba9-21559007f3c1",
    "initiated_by": "209f5b13-dc53-48b8-8965-115a8f0538e4"
}

{
    "amount":100,
    "to_account": "209f5b13-dc53-48b8-8965-115a8f0538e4",
    "from_account": "a5cea467-1bd6-4c47-9ba9-21559007f3c1",
    "initiated_by": "a5cea467-1bd6-4c47-9ba9-21559007f3c1"
}
"""

class PaymentAPI(APIView):
    """ Payment transactions related APIs """
    
    def get(self, request, format=None):
        """ fetches all Payment objects """

        payments = Payment.objects.all()
        serializer = PaymentSerializer(payments, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        """ creates payment objects
            :: amount: `float` transaction amount value
            :: from_account: `string` guid for from account
            :: to_acount: `string` guid for recipient
            :: initiated_by: `string` guid for initiator of transaction
         """
        
        serializer = PaymentSerializer(data=request.data)
        if serializer.is_valid():
            data = request.data
            # create 2 payment objects, corresponding to 'from' & 'to' accouts
            logger.debug("Valid Data: %s" %(request.data))
            serializer.create_incoming_payment(data)
            serializer.create_outgoing_payment(data)

            return Response(status=status.HTTP_200_OK)
        else:
            logger.debug("Invalid data: %s" %serializer.errors)
            return Response(status=status.HTTP_400_BAD_REQUEST, 
                            data=serializer.errors)
        