from django.middleware import csrf

from ...models.Response import Response


def get_token(req):
    return Response.success('OK', {'token': csrf.get_token(req)})
