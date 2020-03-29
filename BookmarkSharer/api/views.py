from django.shortcuts import render

# Create your views here.
from .service import test


def test_ping(req):
    return test.ping(req)
