# serializers.py
from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # Specify fields to include in the serialized representation
        fields = ['id', 'email', 'username', 'password', 'date_joined', 'last_login', 'is_active', 'content']
        extra_kwargs = {
            # Password should not be included in serialized data
            'password': {'write_only': True},
            # Set default value for is_active field
            'is_active': {'default': True},
            # Ensure content is not required
            'content': {'required': False},  
        }

    def create(self, validated_data):
        # Create a new user instance with validated data
        user = User.objects.create(
            email=validated_data['email'],
            username=validated_data['username'],
            is_active=validated_data.get('is_active', True),
            # Set default empty string if content is not provided
            content=validated_data.get('content', ""),  
        )
        # Set password and save user
        user.set_password(validated_data['password'])
        user.save()
        return user
