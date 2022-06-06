from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from embed_video.fields import EmbedVideoField


class Post(models.Model):

    title = models.CharField(max_length=150)
    url = EmbedVideoField(blank=True)
    content = models.TextField(blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=250, unique_for_date='published')  # require that this field be unique for the value of the published  field
    published = models.DateTimeField(default=timezone.now)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)


    class Meta:
        ordering = ['-published']

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class Comment(models.Model):
    
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=250)
    body = models.TextField(blank=True)
    email = models.EmailField()
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)
    

    class Meta:
        ordering = ['created']

    def __str__(self):
        return f'Comment by {self.name} on {self.post}'
    