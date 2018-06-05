from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

# Create your models here.

    
def get_sentinel_user():
    return get_user_model().objects.get_or_create(username='deleted')[0]

class post(models.Model):
    title = models.CharField(max_length=70)
    text = models.CharField(max_length=3750)
    date = models.DateTimeField('published')
    user = models.ForeignKey(User, on_delete=models.SET(get_user_model))
    