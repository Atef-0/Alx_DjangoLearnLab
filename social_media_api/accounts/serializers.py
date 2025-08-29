from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import CustomUser
from rest_framework.authtoken.models import Token




class CustomUserSerializer(serializers.ModelSerializer):
    #random_field = serializers.CharField()
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'bio', 'profile_picture', 'followers', 'following']
        exrtra_kwargs = { 'password': {'write_only': True} }

    def validate_username(self, value):
        if get_user_model().objects.filter(username=value).exists():
            raise serializers.ValidationError("Username already exists")
        return value
    
    def create(self, validated_data):
        email = validated_data.get('email')
        bio = validated_data.get('bio', '')
        profile_picture = validated_data.get('profile_picture', None)

        if not email:
            raise serializers.ValidationError("Email is required")
        
        user = get_user_model().objects.create_user(
            username=validated_data['username'],
            email=email,
            password=validated_data['password'],
            bio=bio,
            profile_picture=profile_picture
        )
        Token.objects.create(user=user)
        return user