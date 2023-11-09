from django.urls import path
from . import views

#app_name = blog

urlpatterns = [
    path('post_list', views.ListView.as_view(), name='post_list'),
    path('post_create', views.CreateView.as_view(), name='post_create'),
    path('post_detail/<int:pk>/', views.DetailView.as_view(), name='post_detail'),
    path('post_update/<int:pk>/', views.UpdateView.as_view(), name='post_update'), 
    path('post_delete/<int:pk>/', views.DeleteView.as_view(), name='post_delete'), 
    ]