import json

from django.http import JsonResponse


def ping(req):
    data = {
        'status': 200,
        'msg': 'pong',
        'data': '祝阿里准架构师李俊锋晚安'
    }
    # return JsonResponse(json.dumps(data, ensure_ascii=False), content_type='application/json,charset=utf-8', safe=False)
    # return JsonResponse(data, content_type='application/json,charset=utf-8', charset='utf-8', safe=False)
    # return JsonResponse(data, charset='utf-8')
    return JsonResponse(data, json_dumps_params={'ensure_ascii': False})
