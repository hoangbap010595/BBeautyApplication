"""
    Custom API Response
    Date: 07.07.2020
    Author: lchoang1995@gmail.com
"""
from rest_framework import status
from rest_framework.response import Response


class APIResponse():
    def __init__(self, message, data):
        self.message = message
        self.data = data

    def success(self):
        result = {
            "status": status.HTTP_200_OK,
            "result": "success",
            "message": self.message,
            "data": self.data
        }
        return Response(result, status=status.HTTP_200_OK)

    def error(self):
        result = {
            "status": status.HTTP_500_INTERNAL_SERVER_ERROR,
            "result": "error",
            "message": self.message,
            "data": self.data
        }
        return Response(result, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
