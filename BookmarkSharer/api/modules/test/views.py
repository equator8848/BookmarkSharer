import json

from ...models.Response import Response


def ping(req):
    data = {
        'status': 200,
        'msg': 'pong',
        'data': '阿里架构师李俊锋早上好'
    }
    return Response.success('good job !', data)


def test_json_object(req):
    return Response.success('OK', None)
