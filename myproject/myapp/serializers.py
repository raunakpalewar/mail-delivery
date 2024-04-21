from rest_framework import serializers
from .models import User, EmailDraft, SentEmail

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'is_staff', 'is_active', 'date_joined')
        read_only_fields = ('id', 'is_staff', 'is_active', 'date_joined')
        
class EmailDraftSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailDraft
        fields = '__all__'

class SentEmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = SentEmail
        fields = '__all__'
