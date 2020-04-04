from django.core.cache import cache

from ...models.CacheKey import CacheKey
from ...models.Response import Response


def get_hot_label(req):
    labels = cache.get(CacheKey.HOT_LABELS.value)
    if labels is None:
        return Response.server_error('没有数据', None)
    else:
        return Response.success('获取成功', labels)
