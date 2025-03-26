from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import UserChangeForm as BaseUserChangeForm
from django.utils.translation import gettext_lazy as _

from .models import User


class UserChangeForm(BaseUserChangeForm):
    """
    Custom UserChangeForm for our custom User model that uses email as the unique identifier
    """
    class Meta(BaseUserChangeForm.Meta):
        model = User
        fields = '__all__'


class UserAdmin(BaseUserAdmin):
    """
    Custom UserAdmin for our custom User model that uses email as the unique identifier
    """
    form = UserChangeForm
    ordering = ['email']
    list_display = ['email', 'first_name', 'last_name', 'is_staff', 'is_active']
    search_fields = ['email', 'first_name', 'last_name']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )


# Register the custom User model with the custom UserAdmin
admin.site.register(User, UserAdmin)
