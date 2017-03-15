# coding: utf-8

from django.contrib import admin
from .models import User, Profile
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserAdminCreationForm, UserAdminForm


class ProfileInline(admin.StackedInline):
    model = Profile


class UserAdmin(BaseUserAdmin):

    list_display = [
        'email', 'name', 'is_active', 'is_staff', 'is_superuser', 'date_joined'
    ]
    add_form = UserAdminCreationForm
    add_fieldsets = (
        (None, {
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    form = UserAdminForm
    fieldsets = (
        (None, {
            'fields': ('email',),
        }),
        ('Informações Básicas',{
            'fields': ('name', 'last_login')
        }),
        ('Permissões', {
            'fields': (
                'is_active', 'is_staff', 'is_superuser', 'groups',
                'user_permissions'
            )
        }),
    )
    ordering = ['name',]
    inlines = [ProfileInline,]


admin.site.register(User, UserAdmin)
