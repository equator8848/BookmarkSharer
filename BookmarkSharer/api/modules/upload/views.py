import time

from ..analysis.BookmarkParser import BookmarkParser
from ...models.DataStatus import DataStatus
from ...models.Response import Response
from ...models.models import TLabel, TSite


def upload_bookmark(req):
    bookmark_file = req.FILES.get('bookmark')
    if bookmark_file is None:
        return Response.parameter_error('请上传文件~', None)
    parser = BookmarkParser()
    parser.parse(bookmark_file)
    site_list = parser.get_site_list()
    for site in site_list:
        print(site)
    return Response.success('书签上传成功，感恩您的分享', None)


def insert_site_if_not_exists(site):
    saved_site = TSite.objects.get(base_url=site.get_url)
    if saved_site is None:
        new_site = TSite()
        new_site.name = site.get_title
        new_site.base_url = site.get_url
        new_site.click_num = 0
        new_site.create_time = time.localtime(time.time())
        new_site.modify_time = new_site.create_time
        new_site.status = DataStatus.NORMAL.value
        new_site.save()
        return new_site.id
    else:
        return saved_site.id


def insert_label_if_not_exists(label):
    saved_label = TLabel.objects.get(name='name')
    if saved_label is None:
        new_label = TLabel()
        new_label.name = label
        new_label.status = DataStatus.NORMAL.value
        new_label.create_time = time.localtime(time.time())
        new_label.modify_time = new_label.create_time
        new_label.save()
        return new_label.id
    else:
        return saved_label.id
