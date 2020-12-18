# pylint: disable=E1101
from django.http import HttpResponse
from .models import Post, AuthorProfile, Comment
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import FormMixin
from django.shortcuts import render
from .forms import CommentForm
# Create your views here.

class PostList(ListView): #for creating post cards
    model = Post
    template_name = 'index.html'
    context_object_name = "all_search_results" #to render results in template with "for x in all_search_results"

    def get_queryset(self):
        query = self.request.GET.get('search') #search parameter
        if query:
            result = Post.objects.filter(status=1, title__contains=query).order_by('-created_on') #find a way to search from multiple fields, also implement ajax later
        else:
            result = Post.objects.filter(status=1).order_by('-created_on') #return all posts if empty search parameter
        return result

class PostDetail(FormMixin, DetailView): #for viewing post content, FormMixin is to include forms
    model = Post
    template_name = 'post_detail.html'
    form_class = CommentForm

    def get_success_url(self):
        return self.request.path_info

    def get_context_data(self, **kwargs): # return form in context
        context = super(PostDetail, self).get_context_data(**kwargs)
        context["form"] = self.get_form()
        context["all_comments"] = Comment.objects.filter(active=True)
        return context
    
    def post(self, request, *agrs, **kwargs):
        if request.method == 'POST':
            self.object = self.get_object()
            form = self.get_form()
            if form.is_valid():
                form.save()
                return super(PostDetail, self).form_valid(form)
            else:
                return self.form_invalid(form)        
    
class AuthorDetail(DetailView): #for viewing author info
    model = AuthorProfile
    template_name = 'author_detail.html'

def about_us(request):
    return render(request, "about_us.html")