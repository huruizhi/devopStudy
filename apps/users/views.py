from django.shortcuts import render
from rest_framework import  viewsets
# Create your views here.
from django.contrib.auth import get_user_model
from .serializers import UserSerializer

User = get_user_model()


class UserViewset(viewsets.ReadOnlyModelViewSet):
    """
    retrieve:
        返回指定用户信息
    list:
        返回用户列表
    """
    user = get_user_model()
    queryset = User.objects.all()
    serializer_class = UserSerializer
