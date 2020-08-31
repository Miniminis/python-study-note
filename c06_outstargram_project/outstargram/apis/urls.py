from django.urls import path

from .views import UserCreateView, UserLoginView, UserLogout

urlpatterns = [
    path('v1/users/create/', UserCreateView.as_view(), name='apis_v1_user_create'),
    path('v1/users/login/', UserLoginView.as_view(), name='apis_v1_user_login'),
    path('v1/users/logout/', UserLogout.as_view(), name='apis_v1_user_logout')
]
