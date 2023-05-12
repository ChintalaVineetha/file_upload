from django.urls import path
from django.contrib import admin
from django.conf import settings
from .views import FileView
from django.conf.urls.static import static
urlpatterns = [
  path('upload/', FileView.as_view(), name='file-upload'),
]
