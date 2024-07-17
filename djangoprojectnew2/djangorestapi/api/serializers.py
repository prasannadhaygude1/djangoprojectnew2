from rest_framework import serializers
from django.contrib.auth.models import User
from .models import client

from .models import Project
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
class clientserializer(serializers.Serializer):
    client_name = serializers.CharField(max_length=100)
    created_at = serializers.IntegerField()
    created_by = serializers.CharField(max_length=100)

    def create(self,validate_data):
        return client.objects.create(**validate_data)

class ProjectSerializer(serializers.ModelSerializer):
    users = UserSerializer(many=True, read_only=True)
    created_by = serializers.ReadOnlyField(source='created_by.username')

    class Meta:
        model = Project
        fields = ['id', 'project_name', 'client', 'users', 'created_at', 'created_by']


