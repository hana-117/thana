from django.urls import path
from .views import HomeView, ProfileEditView, AccountListView, FollowList

app_name = 'accounts'

urlpatterns = [
   path('home/', HomeView.as_view(), name='home'),
   path('edit_profile/', ProfileEditView.as_view(), name='edit_profile'), # 追加
   path('accountlist/', AccountListView.as_view(), name='accountlist'),
   path('followlist/<int:pk>', FollowList.as_view(), name='followlist'),
]
