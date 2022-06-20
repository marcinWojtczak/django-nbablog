from rest_framework import serializers
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from users.models import Profile


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    password2 = serializers.CharField(style={"input_type": "password"}, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'password2', 'email']
        extra_kwargs = {
            'password': {'write_only': True} # to hide the password field
        }

    #overriding save check if password2 == pasword
    def save(self):
        new_user_account = User(
            email = self.validated_data['email'],
            username = self.validated_data['username']
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'error': 'The two password fields didn’t match.'})
        new_user_account.set_password(password)
        new_user_account.save()
        return new_user_account


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'email']
        


