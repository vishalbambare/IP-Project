from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.views import generic
from .forms import CommentForm
# Create your views here.

class PostList(generic.ListView): #for creating post cards
    model = Post
    template_name = 'index.html'
    context_object_name = "all_search_results" #to render results in template with "for x in all_search_results"

    def get_queryset(self):
        result = super(PostList, self).get_queryset()
        query = self.request.GET.get('search') #search parameter
        if query:
            result = Post.objects.filter(status=1, title__contains=query).order_by('-created_on') #find a way to search from multiple fields
        else:
            result = Post.objects.filter(status=1).order_by('-created_on') #return all posts if empty search parameter
        return result

class PostDetail(generic.DetailView): #for viewing post content
    model = Post
    template_name = 'post_detail.html'
    #context_object_name = 'all_comments'
    
class AuthorDetail(generic.DetailView): #for viewing author info
    model = AuthorProfile
    template_name = 'author_detail.html'