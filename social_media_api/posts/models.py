from django.db import models
from django.conf import settings
# Create your models here.

class Post(models.Model):
     author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
         on_delete=models.CASCADE,  
         related_name='posts',      
         verbose_name="Author"
     )
     title = models.CharField(max_length=200, verbose_name="Title")
     content = models.TextField(verbose_name="Content")
     created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
     updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")

     def __str__(self):
         return self.title

     class Meta:
         ordering = ['-created_at']

class Comment(models.Model):
    post = models.ForeignKey(
         Post,
         on_delete=models.CASCADE,  
         related_name='comments',    
         verbose_name="Post"
     )
    author = models.ForeignKey(
         settings.AUTH_USER_MODEL,  
         on_delete=models.CASCADE,  
         related_name='comments',   
         verbose_name="Author"
     )
    content = models.TextField(verbose_name="Content")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")

    def __str__(self):
         return f"Comment by {self.author.username} on {self.post.title}"

    class Meta:
         ordering = ['created_at']  

["models.TextField()"]
