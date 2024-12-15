from django.http import HttpResponse
# class AppMaintenanceMiddleware(object):
class ErrorMessageMiddleware(object):
    def __init__(self,get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_exception(self, request, exception):
        return HttpResponse(f'<h1>Currently we are facing some technical problems.<br>The Raised Exception: {exception.__class__.__name__} <br>The Exception Message: {exception}</h1>')

