from django.urls import path

from .views import (UserCreateView, UserLoginView, UserLogout, 
                    ContentCreateView, RelationCreateView, RelationDeleteView, 
                    UserGetView)

urlpatterns = [
    path('v1/users/create/', UserCreateView.as_view(), name='apis_v1_user_create'),
    path('v1/users/login/', UserLoginView.as_view(), name='apis_v1_user_login'),
    path('v1/users/logout/', UserLogout.as_view(), name='apis_v1_user_logout'), 
    path('v1/users/get/', UserGetView.as_view(), name='apis_v1_user_get'),

    path('v1/contents/create/', ContentCreateView.as_view(), name='apis_v1_contents_create'), 

    path('v1/relations/create', RelationCreateView.as_view(), name='apis_v1_relations_create'), 
    path('v1/relations/delete/', RelationDeleteView.as_view(), name='apis_v1_relations_delete'), 
]
