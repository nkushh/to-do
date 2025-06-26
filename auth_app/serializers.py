from rest_framework.serializers import ModelSerializer
from . import models as auth_models

class UserProfileSerializer(ModelSerializer):
	class Meta:
		model = auth_models.UserProfile
		fields = ['id', 'username', 'email', 'password']

	def create(self, validated_data):
		username = validated_data.get('username').lower()
		validated_data['username'] = username
		return super().create(validated_data)