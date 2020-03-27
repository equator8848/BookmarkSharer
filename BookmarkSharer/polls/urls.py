# coding:utf-8
# Created by Equator at 2020/3/27

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index')
]
