from django.contrib import admin
from .models import Page, SiteInfo, Department, Program, Image

admin.site.register(Page)
admin.site.register(SiteInfo)
admin.site.register(Department)
admin.site.register(Program)

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('name',)
