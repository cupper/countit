from django.contrib import admin
from project.models import *

class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'date', 'get_category_list')
    #list_display = ('')


admin.site.register(Category)
admin.site.register(Item, ItemAdmin)
