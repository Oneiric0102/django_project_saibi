from rest_framework import serializers
from .models import Board,User

class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model=Board 
        fields='__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'