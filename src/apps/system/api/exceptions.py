from rest_framework.views import exception_handler
from django.core.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework import status


def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)
    response2 = Response({}, status.HTTP_400_BAD_REQUEST)
    # Now add the HTTP status code to the response.
    if response is not None:
        try:
            response2.data['status'] = status.HTTP_400_BAD_REQUEST
            response2.data['result'] = 'exception'
            if 'detail' in response.data:
                response2.data['message'] = response.data['detail']
                response2.data['data'] = {}
            else:
                errors = {}
                for key, value in response.data.items():
                    props = []
                    for key2 in value:
                        props.append(key2)
                    errors[key] = props
                response2.data['message'] = 'validation error'
                response2.data['data'] = errors
        except:
            # Catch unexpected exceptions
            response2 = Response({}, response.status_code)
            response2.data['status'] = response.status_code
            response2.data['result'] = 'exception'
            response2.data['message'] = 'validation error'
            response2.data['data'] = {}
    return response2
