from django.contrib import admin
from Flowers.models import Image

class ImageAdmin(admin.ModelAdmin):
	pass

admin.site.register(Image, ImageAdmin)
