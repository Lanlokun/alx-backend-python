from rest_framework import serializers
from .models import User, Message, Conversation

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_id', 'username', 'first_name', 'last_name', 'email', 'phone_number']


class MessageSerializer(serializers.ModelSerializer):
    sender = UserSerializer()  # Nested serializer for the sender (User)
    sent_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")  # Format the sent_at field
    
    class Meta:
        model = Message
        fields = ['message_id', 'sender', 'conversation', 'message_body', 'sent_at', 'created_at']

class ConversationSerializer(serializers.ModelSerializer):
    users = UserSerializer(many=True)  # Many-to-many relationship, serialize users
    messages = MessageSerializer(many=True)  # Many-to-one relationship, serialize messages within the conversation

    class Meta:
        model = Conversation
        fields = ['conversation_id', 'participants', 'messages', 'created_at']