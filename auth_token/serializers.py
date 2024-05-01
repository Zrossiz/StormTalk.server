from .models import AuthToken
from rest_framework import serializers

class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthToken
        fields = '__all__'