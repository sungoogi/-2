from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Post(models.Model):
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')

    def __str__(self):
        return self.title