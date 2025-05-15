from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Link to the User model
    bio = models.TextField(blank=True, null=True)  # Optional bio field
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)  # Optional profile picture
    mood_preference = models.CharField(max_length=50, blank=True, null=True)  # Example: User's preferred mood

    def __str__(self):
        return self.user.username