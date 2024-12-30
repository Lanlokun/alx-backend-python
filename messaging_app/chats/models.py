from django.db import models

# Create your models here.

class Conversation(models.Model):
    name = models.CharField(max_length=100)
    participants = models.ManyToManyField('auth.User', related_name='chats')

    def __str__(self):
        return self.name
    
    def last_10_messages(self):
        return self.messages.order_by('-timestamp').all()[:10]
    
    def get_messages_after(self, timestamp):
        return self.messages.filter(timestamp__gt=timestamp)
    
    def get_messages_before(self, timestamp):
        return self.messages.filter(timestamp__lt=timestamp)
    
    def get_messages_between(self, timestamp1, timestamp2):
        return self.messages.filter(timestamp__gt=timestamp1, timestamp__lt=timestamp2)
    
    def get_messages_by_user(self, user):
        return self.messages.filter(user=user)


class Message(models.Model):
    chat = models.ForeignKey(Conversation, related_name='messages', on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User', related_name='messages', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content

class User(models.Model):
    pass
