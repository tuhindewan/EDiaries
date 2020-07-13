from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Blog(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="post_author")
    title = models.CharField(max_length=255, verbose_name="Put A Title")
    slug = models.SlugField(max_length=255, unique=True)
    content = models.TextField(verbose_name="What's on your mind?")
    image = models.ImageField(verbose_name="Image", upload_to='blog_images')
    publish_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="blog_comment")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_comment")
    comment = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment


class Like(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="liked_blog")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="liker_user")