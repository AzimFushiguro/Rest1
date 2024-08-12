from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telegram = models.URLField(null=True, blank=True)
    instagram = models.URLField(null=True, blank=True)
    bio = models.TextField(null=True,blank=True)
    age = models.IntegerField(default=0)
    job = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.user.first_name

# Create your models here.
