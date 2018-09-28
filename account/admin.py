from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from .models import *
from .forms import *

class UserAdmin(auth_admin.UserAdmin):

    fieldsets = (
        (None, {'fields': ('user_key','user_id', 'password')}),
        ('개인 정보', {'fields': ( 'user_name','project','variables',)}),
        ('권한', {'fields': ('is_staff', 'is_superuser')}),
        ('Important dates', {'fields': ('date_joined','last_login')}),
    )
    limited_fieldsets = (
        (None, {'fields': ('user_id',)}),
        ('Personal info', {'fields': ('user_name')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('user_key','user_id','password1', 'password2')}
        ),
    )

    add_form = UserCreationForm

    list_display = ('user_id', 'user_name','get_project_key','variables', 'date_joined')
    list_filter = ('project__project_key',)
    search_fields = ('user_id','user_name',)
    ordering = ('user_id',)
    readonly_fields = ('last_login', 'date_joined',)

    def get_project_key(self, instance):
        return instance.project.project_key

    get_project_key.short_description = 'Project Key'

admin.site.register(User, UserAdmin)