from django.shortcuts import render
# Create your views here.
from .models import Manufacturer, ProductModel, Server, NetworkDeviceModel, IPModel
from rest_framework import viewsets, generics, mixins
from .serializers import ManufacturerSerializer, ProductSerializer, ServerSerializer, IPSerializer, \
    NetworkDeviceSerializers, ServerAutoReportSerializer


class ManufacturerViewSet(viewsets.ModelViewSet):
    """
    retrieve:
        返回指定 厂商 信息
    list:
        返回 厂商 列表
    update:
        更新 厂商 信息
    destroy:
        删除 厂商 资源
    create:
        创建 厂商 资源
    partial_update:
        局部更新 厂商 信息
    """

    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer


class ProductViewSet(viewsets.ModelViewSet):
    """
    retrieve:
        返回指定 设备 信息
    list:
        返回 设备 列表
    update:
        更新 设备 信息
    destroy:
        删除 设备 资源
    create:
        创建 设备 资源
    partial_update:
        局部更新 设备 信息
    """

    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializer


class ServerViewSet(viewsets.ReadOnlyModelViewSet):
    """
    retrieve:
        返回指定 服务器 信息
    list:
        返回 服务器 列表
    """

    queryset = Server.objects.all()
    serializer_class = ServerSerializer


class ServerAutoReportViewSet(viewsets.GenericViewSet,
                              mixins.CreateModelMixin):
    """
    create:
        创建 服务器 资源
    """

    queryset = Server.objects.all()
    serializer_class = ServerAutoReportSerializer


class NetworkDeviceViewSet(viewsets.ReadOnlyModelViewSet):
    """
    retrieve:
        返回指定 服务器 信息
    list:
        返回 服务器 列表
    """

    queryset = NetworkDeviceModel.objects.all()
    serializer_class = NetworkDeviceSerializers


class IPViewSet(viewsets.ReadOnlyModelViewSet):
    """
    retrieve:
        返回指定 服务器 信息
    list:
        返回 服务器 列表
    """

    queryset = IPModel.objects.all()
    serializer_class = IPSerializer


class ServerViewSet(viewsets.ReadOnlyModelViewSet):
    """
    retrieve:
        返回指定 服务器 信息
    list:
        返回 服务器 列表
    """

    queryset = Server.objects.all()
    serializer_class = ServerSerializer

