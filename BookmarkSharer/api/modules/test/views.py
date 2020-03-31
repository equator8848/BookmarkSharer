import json

from ...models.Response import Response


def ping(req):
    data = {
        'status': 200,
        'msg': 'pong',
        'data': '示例api'
    }
    return Response.success('good job !', data)


def test_json_object(req):
    return Response.success('OK', None)
