from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _
from manage_user.models import PTM, AccountUser, Customer, Instansi

# Register your models here.
@admin.register(AccountUser)
class UserAdmin(BaseUserAdmin):
    list_display = ('username','email','role_user', 'is_superuser')
    fieldsets = (
        (None, {'fields': ('username', 'password', 'role_user', 'ptm_location')}),
        (_('Personal info'), {'fields': (
            'first_name', 
            'last_name', 
            'email',
            'profile_picture',)}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'role_user', 'ptm_location'),
        }),
    )

@admin.register(Instansi)
class InstansiAdminView(admin.ModelAdmin):
    list_display = ('id','name')

@admin.register(Customer)
class CUstomerAdminView(admin.ModelAdmin):
    list_display = ('id','cus_id','name')

@admin.register(PTM)
class PtmAdminView(admin.ModelAdmin):
    list_display = ('id','location')
