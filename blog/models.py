from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

        
class Post(models.Model):
    title = models.CharField(max_length=255)
    tag = models.ForeignKey(Category, related_name='posts')
    text_body = models.TextField(max_length=100000)
    post_by = models.ForeignKey(User, related_name='posts')
    post_date = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    message = models.CharField(max_length=10000)
    create_by = models.ForeignKey(User, related_name='comments')
    create_date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, related_name='comments')
