from rest_framework import serializers

from .models import Category, Albums, Photo


class AlbumsListSerializer(serializers.ModelSerializer):
	"""Список альбомов"""
	creator = serializers.SlugRelatedField(slug_field="username", read_only=True)

	class Meta:
		model = Albums
		fields = ("id", "name", "number_photos", "creator")

class AlbumsDetailSerializer(serializers.ModelSerializer):
	"""Полная информация о альбоме"""
	creator = serializers.SlugRelatedField(slug_field="username", read_only=True)

	class Meta:
		model = Albums
		exclude = ("url", )

class AlbumsCreateSerializer(serializers.ModelSerializer):
	"""Добавление альбома"""

	class Meta:
		model = Albums
		fields = "__all__"

class CategoryCreateSerializer(serializers.ModelSerializer):
	"""Добавление тегов"""

	class Meta:
		model = Category
		fields = "__all__"

class PhotoCreateSerializer(serializers.ModelSerializer):
	"""Добавление альбома"""

	class Meta:
		model = Photo
		fields = "__all__"