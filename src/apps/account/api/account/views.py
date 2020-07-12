from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login as django_login, logout as django_logout
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from apps.system.api.responses import APIResponse
from apps.system.api.serializers import UserSerializer
from . import serializers as acc_serializers
from django.contrib.auth.models import User


@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    serializer = acc_serializers.LoginSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    # Get user and login
    user = serializer.validated_data["user"]
    # django_login(request, user)
    serializer = UserSerializer(user)
    # Get token
    token, created = Token.objects.get_or_create(user=user)
    result = {
        "access_token": token.key,
        "created": created,
        "user": serializer.data
    }
    return APIResponse('Đăng nhập thành công', result).success()


@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    serializer = acc_serializers.RegisterSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    # Get user register
    user = serializer.validated_data["user"]
    serializer = UserSerializer(user)
    return APIResponse('Đăng ký thành công', serializer.data).success()


@api_view(['GET', 'POST'])
def logout(request):
    user = request.user
    # Get token
    token = Token.objects.get(user=user)
    token.delete()

    return APIResponse('Đăng xuất thành công', {}).success()


@api_view(['GET'])
def profile(request):
    r_user = request.user
    user = User.objects.get(username=r_user.username)
    # Get detail
    serializer = UserSerializer(user)
    return APIResponse('Thông tin người dùng', serializer.data).success()


@api_view(['POST'])
def chang_password(request):
    serializer = acc_serializers.PasswordSerializer(data=request.data)
    # Get detail
    serializer.is_valid(raise_exception=True)
    # Get user register
    # Check exists user
    user = User.objects.get(username=request.user.username)
    old_password = request.data.get('old_password')
    if not user.check_password(old_password):
        print('check_password')
        return APIResponse("Mật khẩu hiện tại không đúng", {}).error()
        # Create usser
    user.set_password(request.data.get('new_password'))
    user.save()
    serializer = UserSerializer(user)

    return APIResponse('Đổi mật khẩu thành công', serializer.data).success()
