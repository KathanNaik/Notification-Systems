from django.db import models

# Create your models here.
class Templates(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField()
    event = models.ForeignKey('events.Events', on_delete=models.CASCADE, related_name='templates')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name