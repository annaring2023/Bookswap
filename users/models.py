from django.db import models
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    age = models.IntegerField(null=True, blank=True)
    sex = models.CharField(max_length=10, null=True, blank=True)
    country = models.CharField(max_length=50, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    rating = models.FloatField(default=0.0)
    picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"Профіль {self.user.username}"
