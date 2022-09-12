from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from apis.users.models import CustomerAddress

User = get_user_model()


class UserAdmin(BaseUserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm

    list_display = ('email', 'is_staff',  'is_superuser',
                    'date_joined', 'last_login', 'is_active')
    list_filter = ('is_superuser',)
    readonly_fields = ['date_joined', 'last_login']
    fieldsets = (
        (('Credentials'), {'fields': (
            'email', 'password', 'date_joined', 'last_login', 'is_staff', 'is_superuser')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'role', 'phone_number')}),
        ('Groups', {'fields': ('groups',)}),
        ('Permissions', {'fields': ('user_permissions', 'is_active', 'email_support')}),
    )
    add_fieldsets = (
        (('Credentials'), {'classes': ('wide',), 'fields': (
            'email', 'phone_number', 'password1', 'password2'), }),
    )

    search_fields = ('email', 'name', 'phone')
    ordering = ('email',)
    filter_horizontal = ()


class CustomerAddressAdmin(admin.ModelAdmin):
    list_display = ['user', 'street_address', 'city', 'state', 'selected']
    class Meta:
        model = CustomerAddress

admin.site.register(User, UserAdmin)
admin.site.register(CustomerAddress, CustomerAddressAdmin)
