from django.urls import path
from . import views

urlpatterns = [
    path('upload_bookmark', views.upload_bookmark)
]
