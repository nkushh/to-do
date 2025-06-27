from rest_framework.exceptions import ValidationError
from rest_framework import serializers
from . import models as auth_models
from django.contrib.auth.models import Group

class UserProfileSerializer(serializers.ModelSerializer):
	password = serializers.CharField(write_only=True)
	
	class Meta:
		model = auth_models.UserProfile
		fields = ['id', 'username', 'email', 'password']

	def create(self, validated_data):
		username = validated_data.get('username').lower()
		email = validated_data.get('email')
		password = validated_data.get('password')
		
		user = auth_models.UserProfile(username=username, email=email)
		user.set_password(password)
		user.save()
		return user
	
class UserRolesSerializer(serializers.ModelSerializer):
	class Meta:
		model = Group
		fields = ['id', 'name']

	def create(self, validated_data):
		name = validated_data.get('name').upper()
		validated_data['name'] = name
		if Group.objects.filter(name=name).exists():
			raise ValidationError("Role name already exists.")
		return super().create(validated_data)