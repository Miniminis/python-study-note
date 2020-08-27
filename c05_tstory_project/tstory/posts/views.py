from django.shortcuts import render
from django.views.generic import ListView

from .models import TPost

# Create your views here.
class PostListView(ListView):
    # model = TPost
    queryset = TPost.objects.order_by('-created_at')
    template_name = 'posts/post_list.html'
    context_object_name = 'post_list'

