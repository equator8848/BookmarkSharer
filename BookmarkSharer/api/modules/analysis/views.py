from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore, register_job, register_events
from django.core.cache import cache
from ...models.CacheKey import CacheKey
from ...models.HotLabel import HotLabel
from ...models.Response import Response
from ...models.models import TLabel, TSiteLabelRef
from django.core.cache import cache

scheduler = BackgroundScheduler()
scheduler.add_jobstore(DjangoJobStore(), 'default')


@register_job(scheduler, 'interval', id='update_hot_label', hours=12)
def update_hot_label():
    hot_labels = __get_hot_label(100)
    cache.set(CacheKey.HOT_LABELS.value, hot_labels, timeout=None)


def __get_hot_label(size):
    labels = TLabel.objects.all()
    hot_labels = []
    for label in labels:
        hot = HotLabel()
        hot.id = label.id
        hot.name = label.name
        hot.hotPoint = TSiteLabelRef.objects.filter(label_id=label.id).count()
        hot_labels.append(hot)
    hot_labels.sort(key=lambda obj: obj.hotPoint, reverse=True)
    hot_labels = hot_labels[:size]
    return hot_labels


# 手动更新
def update_hot_label_manual(req):
    hot_labels = __get_hot_label(100)
    cache.set(CacheKey.HOT_LABELS.value, hot_labels, timeout=None)
    return Response.success('OK', hot_labels)

def get_labels_by_page_id(req):
    page_id = req.GET.get('pageId')
    labels = cache.get(page_id)
    if labels is None:
        return Response.fail('暂时没有数据，请稍后再刷新吧~')
    return Response.success('获取成功',labels)


register_events(scheduler)
scheduler.start()
