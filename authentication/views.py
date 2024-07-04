from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from .models import User
from .serializers import UserSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework.authtoken.models import Token

@api_view(['POST'])
@permission_classes([AllowAny])  # In register all users can request
def Register(request):
    password = request.data.get('password')
    request.data['password'] = make_password(password)
    serializer = UserSerializer(data=request.data) 
    if serializer.is_valid():
        user = serializer.save()
        Token.objects.create(user=user)  # Create a token for the new user
        return Response('User created!', status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([AllowAny]) # In login all users can request 
def Login(request):
    email = request.data.get('email')
    password = request.data.get('password')
    user = authenticate(username=email, password=password)
    if user is None:
        return Response('Email or password is Invalid', status=status.HTTP_400_BAD_REQUEST)
    else:
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key}, status=status.HTTP_200_OK)
