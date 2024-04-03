from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from django.views.generic.base import TemplateView
from django.views.generic.edit import UpdateView # 追加
from django.views.generic import ListView
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin # 追加
from .models import CustomUser, Connection
from .forms import ProfileForm  # 追加


class HomeView(TemplateView):
    template_name = 'account/home.html'
   
class ProfileEditView(LoginRequiredMixin, UpdateView):
    template_name = 'account/edit_profile.html'
    model = CustomUser
    form_class = ProfileForm
    success_url = '/accounts/edit_profile/'
  
    def get_object(self):
        return self.request.user
    
  
  #ここから下
    
class FollowBase(LoginRequiredMixin, View):
    """フォローのベース。リダイレクト先を以降で継承先で設定"""
    def get(self, request, *args, **kwargs):
        pk = self.kwargs['pk']
        target_user = CustomUser.objects.get(pk=pk)

        my_connection = Connection.objects.get_or_create(user=self.request.user)

        if target_user in my_connection[0].following.all():
            obj = my_connection[0].following.remove(target_user)
        else:
            obj = my_connection[0].following.add(target_user)
        return obj


class FollowList(FollowBase):
    """AllUserページでフォローした場合"""
    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        
        return redirect('accountlist')
    
    #ここまで
    
  
class AccountListView(LoginRequiredMixin, ListView):
    template_name = 'account/accountlist.html'
    model = CustomUser
    paginate_by = 5

    def get_queryset(self):
        qs = CustomUser.objects.exclude(id=self.request.user.id)
        return qs
    
    
    
#    def get_context_data(self, **kwargs):
#        context = super().get_context_data(**kwargs)
#        context['connection'] = Connection.objects.get_or_create(user=self.request.user)
#        return context
   
