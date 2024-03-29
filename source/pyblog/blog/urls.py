from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('profile/<slug:slug>/', views.AuthorDetail.as_view(), name='author_detail'),
    path('team/about/', views.about_us)
]