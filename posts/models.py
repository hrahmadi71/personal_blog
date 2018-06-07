from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

    
def get_sentinel_user():
    return get_user_model().objects.get_or_create(username='deleted')[0]

class Post(models.Model):
    title = models.CharField(max_length=70)
    text = models.CharField(max_length=3750)
    date = models.DateTimeField('published')
    user = models.ForeignKey(User, on_delete=models.SET(get_user_model))
    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    score = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    text = models.CharField(max_length=255)
    display = models.BooleanField()
    def __str__(self):
        return "From {}; --> {}".format(self.full_name, self.post)