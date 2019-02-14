from django.db import models
from django.utils import timezone

class Post(models.Model):
    """
    A single Bog Post
    """
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=T)