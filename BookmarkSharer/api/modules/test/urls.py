from django.urls import path
from . import views

urlpatterns = [
    path('ping', views.ping),
    path('test_json_object', views.test_json_object)
]
