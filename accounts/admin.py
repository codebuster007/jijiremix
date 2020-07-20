from django.contrib import admin
from .models import ORMUser
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'residence_state')
    readonly_fields = ('password', 'created_at', 'updated_at', )
    
admin.site.register(ORMUser, UserAdmin)