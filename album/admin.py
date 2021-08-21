from django.contrib import admin
from .models import Category, Albums, Photo


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	list_display = ("name", "url")
	

@admin.register(Albums)
class AlbumsAdmin(admin.ModelAdmin):
	list_display = ("name", "number_photos", "date_creation",)
	list_filter = ("number_photos", "date_creation",)
	readonly_fields = ("url", "date_creation", "number_photos", "creator", )


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
	list_display = ("name", "image", "resized",)
	list_filter = ("tag__name", "date_creation",)
	readonly_fields = ("date_creation", "original_sizes", "resized")