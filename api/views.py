from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ClienteSerializer

from .models import Cliente


# Create your views here.
@api_view(['GET'])
def api_def_cliente_view(request, name):
    cliente = Cliente.objects.get(name=name)
    serializer = ClienteSerializer(cliente)
    return Response(serializer.data)


@api_view(['PUT'])
def api_update_cliente_view(request, name):
    cliente = Cliente.objects.get(name=name)
    serializer = ClienteSerializer(cliente, data=request.data)
    data = {}
    if serializer.is_valid():
        serializer.save()
        data["sucess"] = "Update sucessful"
        return Response(data=data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def api_delete_cliente_view(request, name):
    cliente = Cliente.objects.get(name=name)
    operation = cliente.delete()
    data = {}
    if operation:
        data["sucess"] = 'delete sucessful'
    else:
        data["failure"] = 'delete failed'
    return Response(data=data)


@api_view(['POST'])
def api_create_cliente_view(request):
    serializer = ClienteSerializer(data=request.data)
    data = {}
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
