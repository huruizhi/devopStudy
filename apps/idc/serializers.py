from rest_framework import serializers
from .models import Idc


class IdcSerializer(serializers.Serializer):
    """
    Idc 序列化类
    """

    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True, max_length=32, label="机房名称",  help_text="机房名称")
    address = serializers.CharField(required=True, max_length=256, label="机房地址",  help_text="机房地址")
    phone = serializers.CharField(required=True, max_length=15, label="电话号码",  help_text="电话号码")
    email = serializers.EmailField(required=True, max_length=50, label="邮箱",  help_text="邮箱")
    letter = serializers.CharField(required=True, max_length=5, label="机房缩写", help_text="机房缩写")

    def create(self, validated_data):
        return Idc.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.address = validated_data.get("address", instance.name)
        instance.phone = validated_data.get("phone", instance.name)
        instance.email = validated_data.get("email", instance.name)
        instance.save()
        return instance
