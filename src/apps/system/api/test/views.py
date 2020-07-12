import datetime
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from apps.system.api.responses import APIResponse
from django.core.mail import EmailMessage

@api_view(['GET'])
@csrf_exempt
def test(request):
    user = request.user
    data = [{'id': i, 'name': 'Number: {}'.format(i)} for i in range(10)]
    email = EmailMessage(subject='choi thu 3 cai mai', body='<h1>Ahihi con ga ne</h1>', to=['lchoang1995@gmail.com'], cc=['bbeauty202079@gmail.com'])
    email.content_subtype = 'html'
    email.send()
    result = {
        'dateTime': datetime.datetime.now(),
        'user': user.username,
        'sendmail': 'Test send mail to: {}'.format(email.to),
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
