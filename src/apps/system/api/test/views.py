import datetime
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from apps.system.api.responses import APIResponse


@api_view(['GET'])
@csrf_exempt
def test(request):
    user = request.user
    data = [{'id': i, 'name': 'Number: {}'.format(i)} for i in range(10)]
    result = {
        'dateTime': datetime.datetime.now(),
        'user': user.username,
        'data': data
    }
    return APIResponse("test thông tin api", result).success()

@api_view(['POST'])
@csrf_exempt
def test_post(request):
    username = request.data.get('username', None)
    email = request.data.get('email', None)
    result = {
        'dateTime': datetime.datetime.now(),
        'username': username,
        'email': email
    }
    return APIResponse("test thông tin api", result).success()
