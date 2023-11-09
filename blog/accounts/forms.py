from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class MyUserChangeForm(UserChangeForm):
  class Meta:
    model = CustomUser
    fields = '__all__'

class MyUserCreationForm(UserCreationForm):
  class Meta:
    model = CustomUser
    fields = ('email',)


class ProfileForm(forms.ModelForm):
   def __init__(self, *args, **kwargs):
       super(ProfileForm, self).__init__(*args, **kwargs)
       for field in self.fields.values():  # bootstrapで使用するform-controlクラス
           field.widget.attrs['class'] = 'form-control'
           
   class Meta:
       model = CustomUser
       fields = ('nickname', 'email', 'avatar')
       help_texts = {
           'nickname': "ユーザーネーム",
           'email': None,
       }