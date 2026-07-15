from rest_framework import serializers

from django.contrib.auth.password_validation import validate_password

from django.contrib.auth.models import User
from account.models import (Account,
                            Employee,
                            Guest)

       
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email"]

class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = '__all__'
        
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password2')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn’t match."})
        return attrs

    def create(self, validated_data):
        validated_data.pop('password2')
        password = validated_data.pop('password')
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()

        Account.objects.create(user=user)

        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    
class PasswordChangeSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password1 = serializers.CharField(required=True)
    new_password2 = serializers.CharField(required=True)
    
    
class EmployeeSimpleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Employee
        fields = '__all__'


class EmployeeSerializer(serializers.ModelSerializer):
    account_related=AccountSerializer(required=False)
    
    class Meta:
        model = Employee
        fields = '__all__'
        
class GuestSimpleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Guest
        fields = '__all__'


class GuestSerializer(serializers.ModelSerializer):
    account_related=AccountSerializer(required=False)
    
    class Meta:
        model = Guest
        fields = '__all__'