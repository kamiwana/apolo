from rest_framework import serializers
from .models import *

class AccountSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = (
           'id','user_key', 'user_id','password', 'user_name', 'project','variables','date_joined',)
        read_only_fields = ['date_joined','id']


class AccountUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('user_name','project','variables',)