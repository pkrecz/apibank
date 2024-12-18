# -*- coding: utf-8 -*-

from rest_framework import status
from django.http import JsonResponse


class ExceptionMiddleware(object):
    
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_exception(self, request, exception):
        data = {
            "code": "server_error",
            "message": ("Internal server error."),
            "error": {
                "type": str(type(exception)),
                "message": str(exception)
            }
        }
        return JsonResponse(data=data, status=status.HTTP_400_BAD_REQUEST)
