from django.urls import path
from . import views

urlpatterns = [
    path('', views.ListTodoView.as_view(), name = 'list'),
    path('todo/<int:pk>/detail/', views.DetailTodoView.as_view(), name = 'detail-todo'),
    path('todo/create/', views.CreateTodoView.as_view(), name = 'create-todo'),
    path('todo/<int:pk>/update/', views.UpdateTodoView.as_view(), name = 'update-todo'),
    path('todo/<int:pk>/delete/', views.DeleteTodoView.as_view(), name = 'delete-todo'),
]