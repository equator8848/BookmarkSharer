import time
from datetime import datetime
from ..analysis.BookmarkParser import BookmarkParser
from ...models.DataStatus import DataStatus
from ...models.Response import Response
from ...models.models import TLabel, TSite, TSiteLabelRef


def upload_bookmark(req):
    bookmark_file = req.FILES.get('bookmark')
    if bookmark_file is None:
        return Response.parameter_error('请上传文件~', None)
    parser = BookmarkParser()
    parser.parse(bookmark_file)
    site_list = parser.get_site_list()
    for site in site_list:
        site_is_exists, site_id = insert_site_if_not_exists(site)
        if not site_is_exists:
            for label in site.get_labels:
                label_is_exists, label_id = insert_label_if_not_exists(label)
                insert_site_label_ref(site_id, label_id)
    return Response.success('书签上传成功，感恩您的分享', None)


# 插入站点
def insert_site_if_not_exists(site):
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
def insert_label_if_not_exists(label):
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


def insert_site_label_ref(site_id, label_id):
    ref = TSiteLabelRef()
    ref.site_id = site_id
    ref.label_id = label_id
    ref.status = DataStatus.NORMAL.value
    ref.create_time = datetime.now()
    ref.save()
