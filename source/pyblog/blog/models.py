# pylint: disable=E1101
import uuid, os
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

#functions to save images for posts and author profiles
def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "{}.{}".format(uuid.uuid4(), ext)
    return os.path.join('posts', filename)

def get_author_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "{}.{}".format(uuid.uuid4(), ext)
    return os.path.join('authors', filename)

#author profile
class AuthorProfile(models.Model):
    
    author = models.ForeignKey(User, on_delete=models.CASCADE,related_name='blog_posts')
    slug = models.SlugField(max_length=200, unique=True, default="custom-url-for-profile")
    bio = models.TextField(default="bio")
    image = models.ImageField(upload_to=get_author_file_path, default='https://via.placeholder.com/300')

    def __str__(self):
        return self.author.username

#post
class Post(models.Model):
    
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(AuthorProfile, on_delete = models.CASCADE, related_name='author_profile')
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    image = models.ImageField(upload_to=get_file_path, default='https://via.placeholder.com/300')
#add category
    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

#comment
class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return self.body