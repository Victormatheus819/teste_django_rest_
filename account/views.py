from django.shortcuts import render

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import AccountSerializer

from .models import Account


# Create your views here.
@api_view(['POST'])
def registration_view(request):
    serializer = AccountSerializer(data=request.data)
    data = {}
    if serializer.is_valid():
        account = serializer.save()
        data['response'] = 'succesfully registered a new user'
        data['email'] = account.email
        data['username']= account.username
    else:
        data= serializer.errors
    return Response(data)


