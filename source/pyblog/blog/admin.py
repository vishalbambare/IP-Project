from django_summernote.admin import SummernoteModelAdmin
from django.contrib import admin
from .models import AuthorProfile, Post, Comment
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

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'post', 'created_on', 'active',)
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['remove_comment']

    def remove_comment(self, request, queryset):
        queryset.update(active=False) 

admin.site.register(Post, PostAdmin)
admin.site.register(AuthorProfile, AuthorProfileAdmin)