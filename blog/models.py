from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class blog(models.Model):
    title = models.CharField(max_length=150)
    artical = models.TextField()
    photo = models.ImageField(upload_to='blog')
    date_of_post = models.DateTimeField(default = timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title