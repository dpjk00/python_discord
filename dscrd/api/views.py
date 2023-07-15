from rest_framework.decorators import api_view
from rest_framework.response import Response
from dscrd.models import Channel
from rest_framework import status
from rest_framework import permissions
from rest_framework.views import APIView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .serializers import ChannelSerializer, RegistrationSerializer, UserSerializer, LoginSerializer
from . import serializers


@api_view(['GET'])
def get_routes(request):
    routes = [
        'GET /api',
        'GET /api/channels',
        'GET /api/channels/:id'
    ]
    return Response(routes)

@api_view(['GET'])
def get_channels(request):
    channels = Channel.objects.all()
    serializer = ChannelSerializer(channels, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_channel(request, pk):
    channel = Channel.objects.get(id=pk)
    serializer = UserSerializer(channel, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def get_users(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def registration_view(request):
    serializer = RegistrationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login_view(request):
    serializer = LoginSerializer(data=request.data)
    if serializer.is_valid(): 
        username = serializer.validated_data['username']
        password = serializer.validated_data['password']
        user = authenticate(username=username, password=password)
        login(request, user)
        if user:
            return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)