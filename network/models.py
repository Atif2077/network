from django.contrib.auth.models import AbstractUser
from django.db import models
from django import forms


class User(AbstractUser):
    id = models.AutoField(primary_key=True, unique=True)
    pass


class Post(models.Model):
    user = models.CharField(("username here"), max_length=64)
    post_id = models.AutoField(("id"), unique=True, primary_key=True)
    post = models.TextField(("Enter your post here"))
    time = models.DateTimeField(auto_now_add=True)
    likes_no = models.IntegerField(default=0)
    comments = models.IntegerField(default=0)
    liking = models.ManyToManyField("user", blank=True)
    def __str__(self):
        return f"{self.user} has posted this one"
    
class Statistics_user(models.Model):
    user = models.CharField(("user"), max_length=64, default="user")
    bio = models.TextField(("Your bio here"), default="My bio is this")
    following = models.ManyToManyField("user", blank=True)
    liking = models.ManyToManyField("Post", blank=True)
    profile_img = models.CharField(max_length=2048,default="https://th.bing.com/th/id/OIP.Z5BlhFYs_ga1fZnBWkcKjQHaHz?rs=1&pid=ImgDetMain")
    def __str__(self):
        return f"This will give you profile data"
    
class Post_comments(models.Model):
    comment_id = models.IntegerField(unique=False)
    user = models.CharField(("user"), max_length=64)
    comments = models.CharField("Comments", max_length=1024, blank=False)
    time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.user} has commented on this"