from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from .models import Category, Albums, Photo
from .serializers import AlbumsListSerializer, AlbumsDetailSerializer, AlbumsCreateSerializer, PhotoCreateSerializer, CategoryCreateSerializer
from django.contrib.auth import get_user_model
from translate import Translator
from .service import AlbumsFilter

import re


translator = Translator(to_lang="English", from_lang="ru")



class AlbumsListView(generics.ListAPIView):
	"""Вывод списка альбомов"""
	serializer_class = AlbumsListSerializer
	filter_backends = (DjangoFilterBackend,)
	filterset_class = AlbumsFilter
	permission_classes = [permissions.IsAuthenticated]

	def get_queryset(self):
		album = Albums.objects.filter(creator__username=self.request.data['username'])
		return album


class AlbumsDetailView(generics.ListAPIView):
	"""Вывод полного списка альбомов"""
	serializer_class = AlbumsDetailSerializer

	def get_queryset(self):
		album = Albums.objects.filter(id=re.search(r'(?<=albums/)([^/>]+)', self.get_serializer().context['request'].path).group(0), creator__username=self.request.data['username'])
		return album


class AlbumsCreateView(APIView):
	"""Добавление альбома"""
	def post(self, request):
		album = AlbumsCreateSerializer(data=request.data)
		request.data._mutable = True
		album.initial_data['creator'] = get_user_model().objects.get(username=self.request.user).id
		album.initial_data["url"] = f"{get_user_model().objects.get(id=album.initial_data['creator'])}-{(translator.translate(album.initial_data['name'])).replace(' ', '-')}"
		request.data._mutable = False
		if album.is_valid():
			album.save()
		return Response(status=201)

class CategoryCreateView(APIView):
	"""Добавление альбома"""
	def post(self, request):
		album = CategoryCreateSerializer(data=request.data)
		album._mutable = True
		album.initial_data["url"] = (translator.translate(album.initial_data['name'])).replace(' ', '-')
		album._mutable = False
		if album.is_valid():
			album.save()
		return Response(status=201)

class PhotoCreateView(APIView):
	"""Добавление отзыва к фильму"""
	def post(self, request):
		photo = PhotoCreateSerializer(data=request.data)
		if photo.is_valid():
			photo.save()
		return Response(status=201)

# {
# "creator": 1,
# "name": "тест1"
# }

# {
# "album": 1,
# "tag": 1,
# "name": "Имя",
# "text": "Описание",
# "image": "file:///C:/Users/sosed/OneDrive/Изображения/1.jpg"
# }