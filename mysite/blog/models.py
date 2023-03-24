from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify
from django.urls import reverse
from embed_video.fields import EmbedVideoField


class Post(models.Model):

    title = models.CharField(max_length=150)
    url = EmbedVideoField(blank=True)
    content = models.TextField(blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=100, blank=True, null=True)  # require that this field be unique for the value of the published  field
    published = models.DateTimeField(default=timezone.now)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    # def save(self, *args, **kwargs):
    #     if self.slug is None:
    #         self.slug = slugify(self.title)
    #     super().save(*args, **kwargs)
    class Meta:
        ordering = ['-published']

    def __str__(self):
        return self.title

    # tell django how to find url to any specific instance of the post
    def get_absolute_url(self):
        #return reverse('post-detail', kwargs={'pk': self.pk})
        return reverse('post-detail', kwargs={'slug': self.slug}) # reverse return the full URL to that rout as a string

    def save(self, *args, **kwargs):
        if self.slug is None:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)


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

    
    


    