from django.db import models
from users.models import User


class Chat(models.Model):
    """
    Model representing a chat instance.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='chats')
    title = models.TextField(null=True, blank=True)


class Message(models.Model):
    """
    Model representing a message within a chat.
    """
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name='messages')
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    answer = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)


class UserFile(models.Model):
    """
    Model representing a user file uploaded in association with a user.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='userfile')
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to='message_files/')
    content = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username}'s files"

