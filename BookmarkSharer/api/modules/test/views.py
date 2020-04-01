
from ...models.Response import Response
from datetime import date, datetime
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
    t_test.birthday = datetime.now()
    t_test.save()
    return Response.success("注册成功", {
        '用户UID': t_test.id
    })


def get_birthday_by_name(req):
    name = req.GET.get('name')
    if name is None:
        return Response.parameter_error('parameter is null !', None)
    saved_datas = TTest.objects.filter(name=name)
    if len(saved_datas) == 0:
        return Response.bad_request('No data !', None)
    print('saved_datas============', list(saved_datas))
    return Response.success('OK', list(saved_datas))
