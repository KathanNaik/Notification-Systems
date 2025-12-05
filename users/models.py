from django.db import models

class UserPrefernces(models.Model):
    user_uid = models.CharField(max_length=100, unique=True)
    email_notifications = models.BooleanField(default=True)
    sms_notifications = models.BooleanField(default=False)
    push_notifications = models.BooleanField(default=True)

    def __str__(self):
        return f"Preferences of {self.user.username}"
    
class UserEventHistory(models.Model):
    user_uid = models.CharField(max_length=100)
    event = models.ForeignKey('events.Events', on_delete=models.CASCADE, related_name='user_histories')
    template = models.ForeignKey('templates.Templates', on_delete=models.CASCADE, related_name='user_histories')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.event.title} at {self.timestamp}"
