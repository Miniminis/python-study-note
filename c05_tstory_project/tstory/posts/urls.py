from django.urls import path
from .views import (PostListView, PostCreateView, PostDetailView, 
                        CommentCreateView, post_detail, post_like)

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('write/', PostCreateView.as_view(), name='post_write'),
    path('post/<int:pk>/', post_detail, name='post_detail'),
    path('comment/create/', CommentCreateView.as_view(), name='comment_write'),
    path('post/like', post_like, name='post_like'),
]