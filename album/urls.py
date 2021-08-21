from django.urls import path

from . import views


urlpatterns = [
	path("albums/", views.AlbumsListView.as_view()),
	path("albums/<int:pk>/", views.AlbumsDetailView.as_view()),
	path("add-albums/", views.AlbumsCreateView.as_view()),
	path("add-tags/", views.CategoryCreateView.as_view()),
	path("add-photos/", views.PhotoCreateView.as_view()),
]