from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class PostModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tittle = models.CharField(max_length=50)
    date = models.DateField(default= timezone.now)
    text = models.CharField(max_length=300)
    
    def __str__(self):
        return self.tittle