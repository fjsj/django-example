from django.conf import settings

def site_url(request):
    return dict(site_url=settings.SITE_URL)

def view_name(request):
    if hasattr(request, 'resolver_match') and request.resolver_match:
        namespace = request.resolver_match.namespace
        url_name = request.resolver_match.url_name
        return dict(view_name=namespace + ':' + url_name)
    else:
        return dict()
