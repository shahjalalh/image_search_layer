from django.contrib import admin
from .models import Image, ImageSearch

# Register your models here.

class ImageAdmin(admin.ModelAdmin):
    fields = ('url', 'snippet', 'thumbnail', 'context')
    list_display = ('url', 'snippet', 'thumbnail', 'context')

admin.site.register(Image, ImageAdmin)


class ImageSearchAdmin(admin.ModelAdmin):
    fields = ('term',)
    list_display = ('term', 'when')

admin.site.register(ImageSearch, ImageSearchAdmin)
