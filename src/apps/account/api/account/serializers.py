from rest_framework import serializers, exceptions, status
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from apps.account.models import Profile, Setting


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True, error_messages={
                                     "required": "Tên đăng nhập là bắt buộc", "blank": "Tên đăng nhập không được trống"})
    password = serializers.CharField(required=True, error_messages={
                                     "required": "Mật khẩu là bắt buộc", "blank": "Mật khẩu không được trống"})

    def validate(self, data):
        username = data.get('username', None)
        password = data.get('password', None)

        if username and password:
            user = authenticate(username=username, password=password)

            if user:
                if user.is_active:
                    data["user"] = user
                else:
                    # User is not active
                    raise exceptions.APIException(
                        "Tài khoản đang bị vô hiệu hóa")
            else:
                # Unable to login with given credentials.
                raise exceptions.APIException(
                    "Tên đăng nhập hoặc mật khẩu không đúng", status.HTTP_400_BAD_REQUEST)
        else:
            # Must provide username and password both.
            raise exceptions.APIException(
                "Tên đăng nhập hoặc mật khẩu không hợp lệ")
        return data

    class Meta:
        pass


class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField(required=True, error_messages={
                                     "required": "Tên đăng nhập là bắt buộc", "blank": "Tên đăng nhập không được trống"})
    email = serializers.EmailField()
    password = serializers.CharField(required=True, error_messages={
                                     "required": "Mật khẩu là bắt buộc", "blank": "Mật khẩu không được trống"})
    password_confirm = serializers.CharField(required=True, error_messages={
                                             "required": "Xác nhận mật khẩu là bắt buộc.", "blank": "Xác nhận mật khẩu không được trống"})

    def validate(self, data):
        username = data.get('username', None)
        email = data.get('email', None)
        password = data.get('password', None)
        password_confirm = data.get('password_confirm', None)

        if username is None:
            raise exceptions.APIException("Tên đăng nhập không được trống")
        if password is None:
            raise exceptions.APIException("Mật khẩu không được trống")
        if password != password_confirm:
            raise exceptions.APIException("Mật khẩu không trùng khớp")

        # Check exists user
        try:
            user = User.objects.get(username=username)
            if user:
                raise exceptions.APIException("Tài khoản đã được sử dụng")
        except User.DoesNotExist:
            pass
        # Check exists email
        try:
            user = User.objects.get(email=email)
            if user:
                raise exceptions.APIException("Email đã được đăng ký sử dụng")
        except User.DoesNotExist:
            pass

        # Create usser
        user = User.objects.create_user(
            username=username, email=email, password=password)
        data["user"] = user
        return data

    class Meta:
        pass
