from django.shortcuts import render
from django.contrib.auth import authenticate
from rest_framework import authentication, generics, permissions, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
# MODELS
from . import models as auth_models
from django.contrib.auth.models import Group
from rest_framework.authtoken.models import Token
# SERIALIZERS
from . import serializers as auth_serializers

# Create your views here.
def user_login(request):
	template = 'auth_app/login.html'
	return render(request, template)

def user_signup(request):
	template = 'auth_app/signup.html'
	return render(request, template)

class SignupUserView(generics.CreateAPIView):
	queryset = auth_models.UserProfile.objects.all()
	serializer_class = auth_serializers.UserProfileSerializer

	def perform_create(self, serializer):
		user = serializer.save()
		default_role = Group.objects.get(name='CLIENT')
		user.role = default_role
		user.save()
		# Generate token
		token = Token.objects.create(user=user)
		self.token = token

	def create(self, request, *args, **kwargs):
		response = super().create(request, *args, **kwargs)
		return Response(
			{"token": self.token.key, "user": response.data},
			status=status.HTTP_201_CREATED
		)
	
class LoginView(APIView):
	def post(self, request, *args, **kwargs):
		username = request.data.get('username').lower()
		password = request.data.get('password')

		try:
			user = auth_models.UserProfile.objects.get(username=username)
		except auth_models.UserProfile.DoesNotExist:
			return Response({"detail": "User does not exist!"}, status=status.HTTP_404_NOT_FOUND)
		
		if not user.is_active:
			return Response({"detail": "Account is inactive!"}, status=status.HTTP_403_FORBIDDEN)

		if not user.check_password(password):
			return Response({"detail": "Wrong username/password!"}, status=status.HTTP_400_BAD_REQUEST)

		token, _ = Token.objects.get_or_create(user=user)
		serializer = auth_serializers.UserProfileSerializer(user)
		return Response({
			"token": token.key,
			"user": serializer.data
		}, status=status.HTTP_200_OK)
	
class LogoutView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]

    def post(self, request, *args, **kwargs):
        try:
            # Delete the token to log out the user
            request.user.auth_token.delete()
        except (AttributeError, Token.DoesNotExist):
            return Response({"detail": "Invalid token or already logged out."},
                            status=status.HTTP_400_BAD_REQUEST)

        return Response({"detail": "Successfully logged out."}, status=status.HTTP_200_OK)

class ListCreateRolesView(generics.ListCreateAPIView):
	queryset = Group.objects.order_by('name')
	serializer_class = auth_serializers.UserRolesSerializer
