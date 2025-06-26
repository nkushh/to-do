from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
# MODELS
from . import models as auth_models
from rest_framework.authtoken.models import Token
# SERIALIZERS
from . import serializers as auth_serializers

# Create your views here.
@api_view(['POST'])
def signup_user(request):
	serializer = auth_serializers.UserProfileSerializer(data=request.data )
	if serializer.is_valid():
		serializer.save()
		user = auth_models.UserProfile.objects.get(username=request.data['username'])
		user.set_password(request.data['password'])
		user.save()

		token = Token.objects.create(user=user)
		return Response({"token" : token.key, "user" : serializer.data}, status=status.HTTP_201_CREATED)
	return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login_user(request):
	username = request.data['username'].lower()
	password = request.data['passowrd']
	user = auth_models.UserProfile.objects.get(username=username)
	if not user.check_password(password):
		return Response({"detail" : "Worng username/password!"}, status=status.HTTP_404_NOT_FOUND)
	token, _ = Token.objects.get_or_create(user=user)
	serializer = auth_serializers.UserProfileSerializer(user)
	return Response({"token" : token.key, "user" : serializer.data}, status=status.HTTP_200_OK)
