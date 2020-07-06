from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
import datetime


@api_view(['GET'])
@csrf_exempt
def test(request):
    user = request.user
    data = [{'id': i, 'name': 'Number: {}'.format(i) } for i in range(10)]
    result = {'dateTime': datetime.datetime.now(), 'user': user.username, 'data': data}
    return Response(result, status=status.HTTP_200_OK)
