from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView, DeleteView
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post
from .forms import PostCreateForm, PostUpdateForm
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

class PostCreateView(LoginRequiredMixin, CreateView):
    template_name = 'post/create.html'
    form_class = PostCreateForm
    success_url = reverse_lazy('post:create')

    # formに問題なければ、owner id に自分のUser idを割り当てる     
    # request.userが一つのセットでAuthenticationMiddlewareでセットされている。
    def form_valid(self, form):
        form.instance.owner_id = self.request.user.id
        messages.success(self.request, '投稿が完了しました')
        return super(PostCreateView, self).form_valid(form)
    
    def form_invalid(self, form):
        messages.warning(self.request, '投稿が失敗しました')
        return redirect('post/create')


class PostListView(LoginRequiredMixin, ListView):
    template_name = 'post/postlist.html'
    model = Post
    paginate_by = 5

    def get_queryset(self):
        return Post.objects.all()


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostUpdateForm
    template_name = 'post/update.html'

    def form_valid(self, form):
        messages.success(self.request, '更新完了しました')
        return super(PostUpdateView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('post:update', kwargs={'pk':self.object.id})

    def form_invalid(self, form):
        messages.warning(self.request, '更新が失敗しました')
        return reverse_lazy('post:update', kwargs={'pk':self.object.id})


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'post/delete.html'

    success_url = reverse_lazy('post:create')
    success_message = "投稿は削除されました"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(PostDeleteView, self).delete(request, *args, **kwargs)
        

class MyPostsView(LoginRequiredMixin, ListView):
    template_name = 'post/myposts.html'
    model = Post
    paginate_by = 3

    def get_queryset(self):
        qs = Post.objects.filter(owner_id=self.request.user)
        return qs

    def get_context_date(self, **kwargs):
        context = super().get_context_date(**kwargs)
        qs['my_posts_count'] = qs.count()
        return context
    

class OtherPostsView(ListView):
    template_name ='post/otherposts.html'
    model = Post
    paginate_by = 3
    
    def get(self, request, nickname):
        other_user = get_object_or_404(get_user_model(), nickname=nickname)
        user_posts = Post.objects.filter(owner=other_user)
        return render(request, self.template_name, {'other_user': other_user, 'user_posts': user_posts})
