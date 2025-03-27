from django.contrib import admin
from .models import User, Statistics_user, Post, Post_comments

# Register your models here.
admin.site.register(User)
admin.site.register(Statistics_user)
admin.site.register(Post)
admin.site.register(Post_comments)
