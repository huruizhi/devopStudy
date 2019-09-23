from django.shortcuts import render
# Create your views here.
from .models import Idc
from rest_framework import viewsets
from .serializers import IdcSerializer


class IdcViewSetV7(viewsets.ModelViewSet):
    """
    retrieve:
        返回指定Idc 信息
    list:
        返回Idc 列表
    update:
        更新 Idc 信息
    destroy:
        删除 Idc 资源
    create:
        创建 Idc 资源
    partial_update:
        局部更新 Idc 信息
    """

    queryset = Idc.objects.all()
    serializer_class = IdcSerializer

    extra_perms_map = {
        'GET': ['idc.view_idc'],
    }
