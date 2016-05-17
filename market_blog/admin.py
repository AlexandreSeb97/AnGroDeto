from django.contrib import admin
from .models import Atik, AutoLink

# Register your models here.


class AtikAdmin(admin.ModelAdmin):
    list_display = ['non_pwodui','seller','pri','deskripsyon','kontak']
    list_filter = ['uploaded']
    search_fields = ['non_pwodui','seller','pri','deskripsyon','kontak','specs']
    date_hierarchy = 'uploaded'
    save_on_top = True
    prepopulated_fields = {'slug': ('non_pwodui',)}

admin.site.register(Atik, AtikAdmin)


class AutoLinkAdmin(admin.ModelAdmin):
    list_display = ['auto_name', 'auto_model','color', 'seller', 'pri', 'kontak']
    list_filter = ['uploaded']
    search_fields = ['auto_name','seller','pri','deskripsyon','kontak','auto_model', 'transmission','specs']
    date_hierarchy = 'uploaded'
    save_on_top = True
    prepopulated_fields = {'slug': ('auto_name',)}

admin.site.register(AutoLink, AutoLinkAdmin)