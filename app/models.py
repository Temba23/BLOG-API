from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=30)


class Tag(models.Model):
    name = models.CharField(max_length=30)

class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=100)
    author = models.ForeignKey(User, related_name="blog_user", on_delete=models.CASCADE)
    creation_date = models.DateTimeField(auto_now=True)
    category = models.ManyToManyField(Category, related_name="blog_category")
    tag = models.ManyToManyField(Tag, related_name="blog_tag")
    

class Comment(models.Model):
    blog = models.ForeignKey(Blog, related_name="blog_comment", on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="user_comment", on_delete=models.CASCADE)
    comment = models.CharField(max_length=100, default="")