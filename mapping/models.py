from django.db import models

class Tweets(models.Model):
    longitude = models.CharField(max_length=20)
    latitude = models.CharField(max_length=20)
    keywords = models.CharField(max_length=20)
    post_time = models.DateTimeField()
# Create your models here.
