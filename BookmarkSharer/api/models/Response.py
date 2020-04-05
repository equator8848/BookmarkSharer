from datetime import datetime
from collections import Iterable
from enum import Enum, unique
from django.http import JsonResponse


# 状态码
@unique
class StatusCode(Enum):
    SUCCESS = 2000
    BAD_REQUEST = 4000
    PARAMETER_ERROR = 4001
    FORBIDDEN = 4003
    SERVER_ERROR = 5000


class Response:
    def __init__(self, status, msg, data):
        self.status = status
        self.msg = msg
        self.data = data

    @staticmethod
    def response(res):
        print(res)
        print(res.__dict__)
        print(Response.__dict__)
        return JsonResponse(res, safe=False,
                            json_dumps_params={'ensure_ascii': False,
                                               'default': lambda obj: obj.strftime('%Y-%m-%d %H:%M:%S') if
                                               isinstance(obj, datetime) else obj.__dict__})

    @staticmethod
    def transfer(obj):
        if isinstance(obj, Iterable):
            temp = []
            for o in obj:
                temp.append(o.__dict__)
            return temp
        else:
            return obj.__dict__

    @staticmethod
    def success(msg, data=None):
        return Response.response(Response(StatusCode.SUCCESS.value, msg, data))

    @staticmethod
    def bad_request(msg, data=None):
        return Response.response(Response(StatusCode.BAD_REQUEST.value, msg, data))

    @staticmethod
    def parameter_error(msg, data=None):
        return Response.response(Response(StatusCode.PARAMETER_ERROR.value, msg, data))

    @staticmethod
    def forbidden(msg, data=None):
        return Response.response(Response(StatusCode.FORBIDDEN.value, msg, data))

    @staticmethod
    def server_error(msg, data=None):
        return Response.response(Response(StatusCode.SERVER_ERROR.value, msg, data))
