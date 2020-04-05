from django.urls import path
from . import views

urlpatterns = [
    path('github_login_callback', views.github_login_callback)
]
