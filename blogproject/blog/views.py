from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from .forms import PostCreateForm
from .models import Post

class ListView(generic.ListView):
    template_name = 'blog/post_list.html'
    model = Post

class CreateView(generic.CreateView):
    model = Post
    form_class = PostCreateForm
    success_url = reverse_lazy('post_list')

class DetailView(generic.DetailView):
    model = Post
    
class UpdateView(generic.UpdateView):
    model = Post
    form_class = PostCreateForm
    success_url = reverse_lazy('post_detail')

class DeleteView(generic.DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')