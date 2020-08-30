from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, FormView, DetailView
from django.urls import reverse
from django.http import HttpResponseRedirect

from .models import TPost, TComment
from .forms import PostForm, CommentForm

# Create your views here.
class PostListView(ListView):
    # model = TPost
    queryset = TPost.objects.order_by('-created_at')
    template_name = 'posts/post_list.html'
    context_object_name = 'post_list'

# @login_required
# @require_POST
class PostCreateView(FormView):
    form_class = PostForm 
    template_name = 'posts/post_write.html'
    success_url = '/' 

    def form_valid(self, form):
        post = TPost.objects.create(
            writer=self.request.user,
            title=form.data.get('title'),
            content=form.data.get('content'),
            image=form.data.get('image')
        )

        return super().form_valid(form)

class PostDetailView(DetailView):
    template_name = 'posts/post_detail.html'
    model = TPost
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm(self.request)
        return context

def post_detail(request, pk):
    post = get_object_or_404(TPost, pk=pk)
    comments = TComment.objects.filter(post=post.id)
    is_liked = False

    if post.likes.filter(id=request.user.id).exists():
        is_liked = True

    return render(request, 'posts/post_detail.html', context={'post' : post, 'form' : CommentForm(request), 'comments' : comments, 'likes': post.total_likes(), 'is_liked' : is_liked}) 

# @login_required
# @require_POST
class CommentCreateView(FormView):
    form_class = CommentForm
    success_url = '/'

    # def get_success_url(self):
    #     return self.request.path

    def form_valid(self, forms):
        tpost = TPost.objects.get(pk=forms.data.get('post')) 
        comment = TComment.objects.create(
            writer=self.request.user,
            post=tpost,
            comment=forms.data.get('comment')
        )
        return super().form_valid(forms)

    def get_form_kwargs(self, **kwargs):
        kw = super().get_form_kwargs(**kwargs)
        kw.update({
            'request': self.request
        })
        return kw

@login_required
@require_POST
def post_like(request):
    post = get_object_or_404(TPost, pk=request.POST.get('post_id'))
    is_liked = post.likes.filter(id=request.user.id).exists()

    if is_liked:
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    
    return HttpResponseRedirect(reverse('post_detail', kwargs={'pk':post.id}))

