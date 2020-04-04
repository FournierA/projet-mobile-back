from django.urls import path
from .views import *

urlpatterns = [
    path('images/', ImagesView.as_view()), # toutes les images uploadée
    path('images/<int:pk>/', OneImageView.as_view()), # une image uploadée identifiée
    path('images/result/', ImagesResultView.as_view()), # top 5 images du CNN
]
