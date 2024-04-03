from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from .models import CustomUser#, Connection
from .forms import MyUserChangeForm, MyUserCreationForm

class MyUserAdmin(UserAdmin):
  fieldsets = (
    (None, {"fields": ("email", "password")}),
    (_("Personal info"), {"fields": ("nickname","avatar")}),
    (_("Permissions"), {
      "fields": (
        "is_active",
        "is_staff",
        "is_superuser",
        "groups",
        "user_permissions"
      )
    }),
    (_("Important dates"), {"fields": ("last_login", "date_joined")}),
  )
  
  add_fieldsets = (
    (None, {
      "classes": ("wide",),
      "fields": ("email", "password1", "password2"),
    }),
  )
  
  form = MyUserChangeForm
  add_form = MyUserCreationForm
  
  list_display = ("email", "nickname", "is_staff")
  list_filter = ("is_staff", "is_superuser", "is_active", "groups")
  search_fields = ("email", "nickname")
  ordering = ("email",)
  
admin.site.register(CustomUser, MyUserAdmin)

'''
@admin.register(Connection)
class ConnectionAdmin(admin.ModelAdmin):
    pass
'''
