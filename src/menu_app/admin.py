from django.contrib import admin
from .models import Menu, MenuItem


class MenuItemInline(admin.TabularInline):
    model = MenuItem
    extra = 1


class MenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ['name', 'description']
    inlines = [MenuItemInline]


class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'menu', 'parent', 'url')
    list_filter = ('menu', 'parent')
    search_fields = ['name', 'url']


admin.site.register(Menu, MenuAdmin)
admin.site.register(MenuItem, MenuItemAdmin)
