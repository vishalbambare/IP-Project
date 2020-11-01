import uuid, os
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "{}.{}".format(uuid.uuid4(), ext)
    return os.path.join('posts', filename)

def get_author_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "{}.{}".format(uuid.uuid4(), ext)
    return os.path.join('authors', filename)

class AuthorProfile(models.Model):
    
    author = models.ForeignKey(User, on_delete=models.CASCADE,related_name='blog_posts')
    bio = models.TextField(default="bio")
    image = models.ImageField(upload_to=get_author_file_path, default='https://via.placeholder.com/300')

    def __str__(self):
        return self.author.username

class Post(models.Model):
    
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(AuthorProfile, on_delete = models.CASCADE, related_name='author_profile')
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    image = models.ImageField(upload_to=get_file_path, default='https://via.placeholder.com/300')

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title