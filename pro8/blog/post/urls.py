from django.urls import path
from .views import PostCreateView, PostListView, PostUpdateView, PostDeleteView, MyPostsView, OtherPostsView

app_name = 'post'

urlpatterns = [
    path('create/', PostCreateView.as_view(), name = 'create'),
    path('postlist/', PostListView.as_view(), name = 'postlist'),
    path('update/<int:pk>', PostUpdateView.as_view(), name = 'update'),
    path('delete/<int:pk>', PostDeleteView.as_view(), name = 'delete'),
    path('myposts/', MyPostsView.as_view(), name = 'myposts'),
    path('otherposts/<str:nickname>/', OtherPostsView.as_view(), name = 'otherposts'),
]