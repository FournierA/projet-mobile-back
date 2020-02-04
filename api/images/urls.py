from django.urls import path
from .views import OneImageView, ImagesView

urlpatterns = [
    path('images', ImagesView.as_view()),
    path('images/<int:pk>', OneImageView.as_view())
]