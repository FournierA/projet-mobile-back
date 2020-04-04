from django.urls import path
from .views import *

urlpatterns = [
    path('images/', ImagesView.as_view()),  # toutes les images uploadée
    # une image uploadée identifiée
    path('images/<int:pk>/', OneImageView.as_view()),
    path('images/result/', ImagesResultView.as_view()),  # top 5 images du CNN
]
