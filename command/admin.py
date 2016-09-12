from django.contrib import admin
from command.models import Gallery


class GalleryAdmin(admin.ModelAdmin):
    list_display = ('name','id', 'photo')

admin.site.register(Gallery, GalleryAdmin)

# Register your models here.
