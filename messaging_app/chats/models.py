import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid

class User(AbstractUser):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.username

class Conversation(models.Model):
    conversation_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    users = models.ManyToManyField(User, related_name='conversations')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Conversation {self.conversation_id} - {', '.join(user.username for user in self.users.all())}"


class Message(models.Model):
    message_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages') 
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name='messages')
    message_body = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
