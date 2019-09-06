from rest_framework import serializers
from .models import ProductModel, Manufacturer, Server, NetworkDeviceModel, IPModel


class ManufacturerSerializer(serializers.ModelSerializer):
    """
    制造商序列化
    """

    class Meta:
        model = Manufacturer
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    """
    设备 序列化
    """
    class Meta:
        model = ProductModel
        fields = "__all__"

    def to_representation(self, instance):
        vendor = instance.vendor
        ref = super(ProductSerializer, self).to_representation(instance)
        ref["vendor"] = {
            "id": vendor.id,
            "name": vendor.vendor_name
        }

        return ref

    def validate(self, attrs):
        return attrs


class ServerAutoReportSerializer(serializers.Serializer):
    """
    服务器序列化 插入
    """
    ip          = serializers.CharField(max_length=15, required=True, )
    hostname    = serializers.CharField(max_length=15, required=True, )
    cpu         = serializers.CharField(max_length=50, required=True, )
    mem         = serializers.CharField(max_length=50, required=True, )
    disk        = serializers.CharField(max_length=200, )
    os          = serializers.CharField(max_length=50, required=True, )
    sn          = serializers.CharField(max_length=50, required=True, )
    uuid        = serializers.CharField(max_length=50, required=True, )
    manufacturer= serializers.CharField(max_length=50, required=True, )
    model_name  = serializers.CharField(max_length=50, required=True, )
    network     = serializers.JSONField(required=True)

    def validate_manufacturer(self, value):
        try:
            value = Manufacturer.objects.get(vendor_name=value)
        except Manufacturer.DoesNotExist:
            value = Manufacturer.objects.create(**{"vendor_name": value})
        return value

    def validate(self, attrs):
        model_name = attrs["model_name"]
        try:
            model_obj = ProductModel.objects.get(model_name=model_name)
        except ProductModel.DoesNotExist:
            model_obj = ProductModel.objects.create(**{
                "model_name": model_name,
                "vendor": attrs["manufacturer"]
            })
        finally:
            attrs["model_name"] = model_obj
            return attrs

    def create(self, validated_data):
        uuid = validated_data["uuid"]
        sn = validated_data["sn"]
        try:
            if uuid.lower() == sn.lower() or sn == '':
                # 虚拟机
                server_obj = Server.objects.get(uuid__icontains=uuid)
            else:
                # 物理机
                server_obj = Server.objects.get(sn__icontains=sn)
        except Server.DoesNotExist:
            # 创建服务器
            return self.create_server(validated_data)
        else:
            # 更新服务器信息
            return self.update_server(server_obj, validated_data)

    def create_server(self, validated_data):
        network = validated_data.pop("network")
        server_obj = Server.objects.create(**validated_data)
        self.check_network_device(network, server_obj)
        return server_obj

    def update_server(self, instance, validated_data):
        instance.ip = validated_data.get("ip", instance.ip)
        instance.hostname = validated_data.get("hostname", instance.hostname)
        instance.cpu = validated_data.get("cpu", instance.cpu)
        instance.mem = validated_data.get("mem", instance.mem)
        instance.disk = validated_data.get("disk", instance.disk)
        instance.os = validated_data.get("os", instance.os)
        instance.save()
        network = validated_data.pop("network")
        self.check_network_device(network, instance)
        return instance

    def check_network_device(self, network, server_obj):
        query_set = server_obj.networkdevicemodel_set.all()
        network_obj_list = list()
        for device in network:
            ips = device.pop("ips")
            try:
                network_obj = query_set.get(mac_address=device["mac_address"])
            except NetworkDeviceModel.DoesNotExist:
                network_obj = self.create_network_device(device, server_obj)
            network_obj_list.append(network_obj)
            self.check_ip_info(ips, network_obj)

        for network_device in set(query_set) - set(network_obj_list):
            network_device.delete()

    def check_ip_info(self, ips, network_obj):
        ip_queryset = network_obj.ipmodel_set.all()
        ip_obj_list = list()
        for ip in ips:
            try:
                ip_obj = ip_queryset.get(ip_addr=ip["ip_addr"])
            except IPModel.DoesNotExist:
                ip_obj = self.create_ip_info(ip, network_obj)
            ip_obj_list.append(ip_obj)

        for ip in set(ip_queryset) - set(ip_obj_list):
            ip.delete()

    def create_ip_info(self, ip, network_obj):
        ip["device"] = network_obj
        return IPModel.objects.create(**ip)

    def create_network_device(self, device, server_obj):
        device["host"] = server_obj
        return NetworkDeviceModel.objects.create(**device)

    def to_representation(self, instance):
        ref = {"ip": instance.ip,
               "hostname": instance.hostname}
        return ref


class ServerSerializer(serializers.ModelSerializer):
    """
    服务器 序列化 只读
    """

    class Meta:
        model = Server
        fields = "__all__"


class NetworkDeviceSerializers(serializers.ModelSerializer):
    """
    网络地址 序列化
    """

    class Meta:
        model = NetworkDeviceModel
        fields = "__all__"


class IPSerializer(serializers.ModelSerializer):
    """
    IP 地址 序列化
    """

    class Meta:
        model = IPModel
        fields = "__all__"


