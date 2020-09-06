from django.shortcuts import render
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from .models import Content, FollowReleation

# Create your views here.

# 로그인 상태로만 접근 가능하기 때문에 자동으로 로그인 페이지로 redirect 처리
@method_decorator(login_required, name='dispatch')      
class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)

        user = self.request.user
        followees = FollowReleation.objects.filter(follower=user).values_list('followee__id', flat=True)
        lookup_user_ids = [user.id] + list(followees)   # 내 게시물 + 내가 팔로우 하는 사람들의 게시물
        context['contents'] = Content.objects.select_related('user').prefetch_related('image_set').filter(
            user__id__in=lookup_user_ids    
        )
        return context


class RelationView(TemplateView):
    template_name='relation.html'