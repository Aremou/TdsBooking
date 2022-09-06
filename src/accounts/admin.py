from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model


from accounts.models import CustomUser, HotelManager, Profile


@admin.register(HotelManager)
class HotelManagerAdmin(admin.ModelAdmin):
    pass


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'gender',
        'country'
    )


User = get_user_model()


class UserAdmin(BaseUserAdmin):

    form = UserChangeForm
    add_form = UserCreationForm
    model = CustomUser
    list_display = ('email', 'first_name', 'last_name', 'tel',
                    'is_admin', 'is_active',)
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('email', 'password', 'first_name', 'last_name')}),
        ('Personal info', {'fields': ('tel',)}),
        ('Permissions', {'fields': ('is_admin', 'is_staff', 'is_manager',
         'is_active', 'is_superuser', 'groups', 'user_permissions',)}),
    )


    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'tel', 'first_name', 'last_name', 'password1', 'password2'),
        }),
    )
    search_fields = ('email',)
    ordering = ('email',)
   




admin.site.register(CustomUser, UserAdmin)


