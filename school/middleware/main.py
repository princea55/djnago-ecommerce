from django.http import HttpResponse


class BlockMobileMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request, *args, **kwargs):
        if not request._get_scheme() == 'http':
            return HttpResponse("Site does not server http request.", status=400)
        return self.get_response(request)


def auth_middleware(get_response):
    def middleware(request):
        print("Authentication middleware")
        if not request._get_scheme() == 'http':
            return HttpResponse("Site does not server http request.", status=400)
        response = get_response(request)
        return response

    return middleware
