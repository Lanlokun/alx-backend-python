from rest_framework import serializers
from .models import User, Conversation, Message
import uuid

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    def get_full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}" if obj.first_name and obj.last_name else obj.username
    
    class Meta:
        model = User
        fields = ['user_id', 'username', 'first_name', 'last_name', 'email', 'phone_number', 'profile_picture', 'status', 'full_name']

class MessageSerializer(serializers.ModelSerializer):
    sender = UserSerializer() 
    sent_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    message_body = serializers.CharField(max_length=2000)
    
    def validate_message_body(self, value):
        """
        Custom validation for message body to check if it's not empty.
        """
        if not value.strip():
            raise serializers.ValidationError("Message body cannot be empty")
        return value

    class Meta:
        model = Message
        fields = ['message_id', 'sender', 'conversation', 'message_body', 'sent_at', 'created_at']
        
class ConversationSerializer(serializers.ModelSerializer):
    users = UserSerializer(many=True)
    messages = MessageSerializer(many=True)
    
    total_messages = serializers.SerializerMethodField()
    
    def get_total_messages(self, obj):
        return obj.messages.count()
    
    def validate_users(self, value):
        """
        Ensure a conversation has at least two users.
        """
        if len(value) < 2:
            raise ValidationError("A conversation must involve at least two users.")
        return value

    class Meta:
        model = Conversation
        fields = ['conversation_id', 'users', 'messages', 'created_at', 'total_messages']
