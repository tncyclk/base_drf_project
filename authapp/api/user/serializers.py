from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

class UserSerializer(ModelSerializer):

    full_name = serializers.SerializerMethodField()

    def get_full_name(self, obj):
        return '{} {}'.format(obj.first_name, obj.last_name) 
    
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name','full_name')