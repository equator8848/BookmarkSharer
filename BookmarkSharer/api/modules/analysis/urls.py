from django.urls import path

from . import views

urlpatterns = [
    # path('update_hot_label', views.update_hot_label),
    path('update_hot_label_manual', views.update_hot_label_manual)
]
