from rest_framework import serializers
from .models import Cabinet
from idc.serializers import IdcSerializer
from idc.models import Idc


class CabinetSerializer(serializers.Serializer):
    """
    Idc 序列化类
    """

    id = serializers.IntegerField(read_only=True)
    idc = serializers.PrimaryKeyRelatedField(many=False, queryset=Idc.objects.all())
    name = serializers.CharField(required=True, max_length=256, label="机柜名称",  help_text="机柜名称")

    def to_representation(self, instance):
        idc_obj = instance.idc
        ref = super(CabinetSerializer, self).to_representation(instance)
        ref["idc"] = {
            "id": idc_obj.id,
            "name": idc_obj.name
        }
        return ref

    def to_internal_value(self, data):
        print(data)
        return super(CabinetSerializer, self).to_internal_value(data)

    def create(self, validated_data):
        return Cabinet.objects.create(**validated_data)
