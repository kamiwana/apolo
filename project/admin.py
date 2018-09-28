from django.contrib import admin
from .models import *
from .forms import *

class ProjectAdmin(admin.ModelAdmin):
    # The forms to add and change user instances

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    # list_per_page = 5
    form = ProjectForm
    list_display = ('project_name','project_key','global_variables',)
    #  list_display_links = ('project_name',)
    # list_editable = ('project_key',)

    search_fields = ('project_name',)
    ordering = ('-timestamp',)
    filter_horizontal = ()
    readonly_fields = ('timestamp',)

# Register your models here.
admin.site.register(Project,ProjectAdmin)