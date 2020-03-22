from django.urls import path
from .views import *

urlpatterns = [
    path('images', ImagesView.as_view()),
    path('images/<int:pk>', OneImageView.as_view()),
    path('images/search/<int:pk>', SearchView.as_view()),
]