from ..analysis.BookmarkParser import BookmarkParser
from ...models.Response import Response


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
