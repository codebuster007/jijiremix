from django.contrib import admin
from .models import ORMItem, ORMBuyer
# Register your models here.

class ItemAdmin(admin.ModelAdmin):
    list_display = ('owner', 'name', 'price', )
    readonly_fields = ('created_at', 'updated_at', )


class BuyerAdmin(admin.ModelAdmin):
    list_display = ('item', 'name', 'email', 'location')


admin.site.register(ORMItem, ItemAdmin)
admin.site.register(ORMBuyer, BuyerAdmin)