from django.urls import path

from . import views

urlpatterns = [
    path('get_hot_label', views.get_hot_label)
]
