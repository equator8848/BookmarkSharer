import logging
import uuid
from datetime import datetime
from ..analysis.BookmarkParser import BookmarkParser
from ...models.DataStatus import DataStatus
from ...models.Response import Response
from ...models.models import TLabel, TSite, TSiteLabelRef
from collections import defaultdict
from django.core.cache import cache
import threading


def upload_bookmark(req):
    is_share = req.POST.get('isShare')
    bookmark_file = req.FILES.get('bookmark')
    if bookmark_file is None:
        return Response.parameter_error('请上传文件~', None)
    parser = BookmarkParser()
    parser.parse(bookmark_file)
    site_list = parser.get_site_list()
    page_id = str(uuid.uuid1())
    threading.Thread(target=__save_labels, args=(page_id, site_list, is_share), name='save_labels').start()
    return Response.success('书签上传成功，感恩您的分享', {
        'pageId': page_id
    })


def __save_labels(page_id, site_list, is_share):
    __save_site_and_label_cache(page_id, site_list)
    if is_share:
        logging.debug("save to mysql ...")
        __save_site_and_label_db(site_list)


def __save_site_and_label_cache(page_id, site_list):
    # 标签 name -> hotPoint 的映射
    labels = defaultdict(lambda: 0)
    for site in site_list:
        for label in site.get_labels:
            labels[label] = labels[label] + 1
    # 保存一天
    labels_list = []
    for key, val in labels.items():
        labels_list.append((key, val))
    # logging.debug(labels_list)
    labels_list.sort(key=lambda obj: obj[1], reverse=True)
    cache.set(page_id, labels_list, timeout=86400)


def __save_site_and_label_db(site_list):
    for site in site_list:
        site_is_exists, site_id = __insert_site_if_not_exists(site)
        if not site_is_exists:
            for label in site.get_labels:
                label_is_exists, label_id = __insert_label_if_not_exists(label)
                __insert_site_label_ref(site_id, label_id)


# 插入站点
def __insert_site_if_not_exists(site):
    saved_sites = TSite.objects.filter(base_url=site.get_url)
    if len(saved_sites) == 0:
        new_site = TSite()
        new_site.name = site.get_title
        new_site.base_url = site.get_url
        new_site.click_num = 0
        new_site.create_time = datetime.now()
        new_site.modify_time = new_site.create_time
        new_site.status = DataStatus.NORMAL.value
        new_site.save()
        return False, new_site.id
    else:
        return True, saved_sites[0].id


# 插入标签
def __insert_label_if_not_exists(label):
    saved_labels = TLabel.objects.filter(name=label)
    if len(saved_labels) == 0:
        new_label = TLabel()
        new_label.name = label
        new_label.status = DataStatus.NORMAL.value
        new_label.create_time = datetime.now()
        new_label.modify_time = new_label.create_time
        new_label.save()
        return False, new_label.id
    else:
        return True, saved_labels[0].id


def __insert_site_label_ref(site_id, label_id):
    ref = TSiteLabelRef()
    ref.site_id = site_id
    ref.label_id = label_id
    ref.status = DataStatus.NORMAL.value
    ref.create_time = datetime.now()
    ref.save()
