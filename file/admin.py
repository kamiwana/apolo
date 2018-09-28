from django.contrib import admin
from .models import *

class FileAdmin(admin.ModelAdmin):
    # The forms to add and change user instances

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.

    list_display = ('file_name','get_project_key','get_user_id','expire_min',)
    list_display_links = ('file_name',)
    list_filter = ('project__project_key',)

    search_fields = ('file_name','project__project_key','user__user_id',)
    ordering = ('-timestamp',)
    filter_horizontal = ()
    readonly_fields = ('timestamp',)

    def get_project_key(self, instance):
        return instance.project.project_key

    def get_user_id(self, instance):
        return instance.user.user_id

    get_project_key.short_description = 'PROJECT KEY'
    get_user_id.short_description = 'USER ID'

# Register your models here.
admin.site.register(File,FileAdmin)