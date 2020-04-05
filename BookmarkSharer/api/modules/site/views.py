from ...models.Response import Response
from ...models.models import TSiteLabelRef, TSite


def get_site_by_label_id(req):
    label_id = req.GET.get('labelId')
    refs = TSiteLabelRef.objects.filter(label_id=label_id)
    if refs is not None:
        sites = []
        for ref in refs:
            site_id = ref.site_id
            site = TSite.objects.filter(id=site_id)
            if site is not None:
                sites.append(site)
        return Response.success("成功获取", sites)
    return Response.bad_request('没有数据')
