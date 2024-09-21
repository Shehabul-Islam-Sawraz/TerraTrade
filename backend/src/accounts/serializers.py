from .models import User, Farmer
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'phone_number', 'address', 'profile_picture', 'role']

class FarmerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farmer
        fields = ['id', 'farmer', 'farm_address', 'has_cold_store', 'description']