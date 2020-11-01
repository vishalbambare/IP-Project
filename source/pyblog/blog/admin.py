from django_summernote.admin import SummernoteModelAdmin
from django.contrib import admin
from .models import *
# Register your models here.

class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'status','created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)

class AuthorProfileAdmin(SummernoteModelAdmin):
    list_display = ('author', 'slug',)
    search_fields = ['author',]
    prepopulated_fields = {'slug': ('author',)}

admin.site.register(Post, PostAdmin)
admin.site.register(AuthorProfile, AuthorProfileAdmin)