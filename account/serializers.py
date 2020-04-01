from rest_framework import serializers
from .models import Account


class AccountSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = Account
        fields = ['username', 'email', 'password', "password2"]
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        account = Account(
            email=self._validated_data['email'],
            username=self._validated_data['username'],
        )
        password = self._validated_data['password']
        password2 = self._validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password': "Passwords must match"})
        account.set_password(password)
        account.save()
        return account
