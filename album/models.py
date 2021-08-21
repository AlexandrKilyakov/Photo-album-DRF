from django.db import models
from datetime import date
from django.urls import reverse
from django.conf import settings
from PIL import Image


class Category(models.Model):
	"""Категории (теги)"""
	name = models.CharField("Категория", max_length=50)
	url = models.SlugField(max_length=160, unique=True, blank=True)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "Категория"
		verbose_name_plural = "Категории"

class Albums(models.Model):
	"""Альбом"""
	creator = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="Создатель", on_delete=models.CASCADE, related_name="creators_album")
	name = models.CharField("Название альбома", max_length=50)
	number_photos = models.PositiveSmallIntegerField("Количество фотографий", default=0)
	url = models.SlugField(max_length=130, unique=True, default='', blank=True)
	date_creation = models.DateField("Дата создания", default=date.today)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse("album_detail", kwargs={"slug": self.url})

	class Meta:
		verbose_name = "Название альбома"
		verbose_name_plural = "Название альбомов"

class Photo(models.Model):
	"""Фотографии"""
	album = models.ForeignKey(Albums, verbose_name="Альбом", on_delete=models.CASCADE, related_name="photos")
	tag = models.ManyToManyField(Category, verbose_name="Список тегов", related_name="tags")
	name = models.CharField("Название", max_length=100)
	text = models.TextField("Описание", max_length=500)
	image = models.ImageField("Изображение", upload_to="image/")
	original_sizes = models.CharField("Оригинальный размер", max_length=9, default='0', blank=True)
	resized = models.CharField("Измененный размер", max_length=8, default='0', blank=True)
	date_creation = models.DateField("Дата создания", default=date.today)

	def __str__(self):
		return self.name

	def save(self, *args, **kwargs):
		if self.image.size <= 5242880:
			img = Image.open(self.image)
			if img.format in ['JPEG', 'PNG']:
				self.original_sizes = f'{img.size[0]}x{img.size[1]}'

				divider = img.size[0] / 150.0 if img.size[0] > img.size[1] else img.size[1] / 150.0
				height = int(img.size[0] / divider)
				wedth = int(img.size[1] / divider)

				self.image = img.resize((height, wedth),Image.ANTIALIAS)
				self.resized = f'{height}x{wedth}'
				return self
			else:
				raise Exception("Только форматы: 'JPEG', 'PNG'")		
		else:
			raise Exception("Больше 5мб")


	class Meta:
		verbose_name = "Фотография"
		verbose_name_plural = "Фотографии"