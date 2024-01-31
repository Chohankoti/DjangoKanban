from rest_framework import serializers
from .models import Users, Tasks, CCode, AccessControl

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'

class TasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = '__all__'

class CCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CCode
        fields = '__all__'

class AccessControlSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccessControl
        fields = '__all__'
