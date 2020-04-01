import json

from ...models.Response import Response
from ...models.forms.TestForm import TestForm
from ...models.models import TTest


def ping(req):
    data = {
        'status': 200,
        'msg': 'pong',
        'data': '示例api'
    }
    return Response.success('good job !', data)


def test_json_object(req):
    return Response.success('OK', None)


def register(req):
    t_test = TTest()
    t_test.name = req.POST.get('name')
    t_test.birthday = req.POST.get('birthday')
    t_test.save()
    return Response.success("注册成功", {
        '用户UID': t_test.id
    })


def get_birthday_by_name(req):
    name = req.GET.get('name')
    if name is None:
        return Response.parameter_error('parameter is null !', None)
    try:
        saved_data = TTest.objects.get(name=name)
    except TTest.DoesNotExist:
        return Response.bad_request('No data !', None)
    return Response.success('OK', saved_data)
