from django.shortcuts import render
from django.views.generic.edit import UpdateView  # 追加
from django.contrib.auth.mixins import LoginRequiredMixin  # 追加
from .models import CustomUser # 追加
from .forms import ProfileEditForm  # 追加

class ProfileEditView(LoginRequiredMixin, UpdateView):
    template_name = 'account/edit_profile.html'
    model = CustomUser
    form_class = ProfileEditForm
    success_url = '/accounts/edit_profile/'

    def get_object(self):
        return self.request.user
