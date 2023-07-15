from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from dscrd.models import Channel
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


class ChannelSerializer(ModelSerializer):
    class Meta:
        model = Channel
        fields = '__all__'

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class RegistrationSerializer(ModelSerializer):

    password = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password']
    
    def save(self):
        user = User(
            username = self.validated_data['username'],
            password = self.validated_data['password'],
        )
        password = self.validated_data['password']

        user.set_password(password)
        user.save()
        return user
    
class LoginSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'password']

    username = serializers.CharField(
        label="username",
        write_only = True
    )

    password = serializers.CharField(
        label="password",
        style={'input_type': 'password'},
        trim_whitespace=False,
        write_only=True
    )

    def validate(self, attrs):
        # Take username and password from request
        username = attrs.get('username')
        password = attrs.get('password')

        if username and password:
            # Try to authenticate the user using Django auth framework.
            user = authenticate(request=self.context.get('request'),
                                username=username, password=password)
            if not user:
                # If we don't have a regular user, raise a ValidationError
                msg = 'Access denied: wrong username or password.'
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = 'Both "username" and "password" are required.'
            raise serializers.ValidationError(msg, code='authorization')
        # We have a valid user, put it in the serializer's validated_data.
        # It will be used in the view.
        attrs['user'] = user
        return attrs