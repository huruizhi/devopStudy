from django.db import models
from idc.models import Idc
from cabinet.models import Cabinet
# Create your models here.


class Manufacturer(models.Model):
    vendor_name = models.CharField("厂商名称", max_length=32, db_index=True, unique=True)
    tel = models.CharField("联系电话", max_length=15, null=True, blank=True)
    mail = models.EmailField('邮箱地址', max_length=50, null=True, blank=True)
    remark = models.CharField("备注", max_length=300, null=True)

    def __str__(self):
        return self.vendor_name

    class Meta:
        db_table = "resources_manufacturer"
        ordering = ["id"]


class ProductModel(models.Model):
    model_name = models.CharField("型号名称", max_length=20)
    vendor = models.ForeignKey(Manufacturer, verbose_name="制造商")

    def __str__(self):
        return "{}-{}".format(self.vendor, str(self.model_name),)

    class Meta:
        db_table = "resources_product_model"
        ordering = ["id"]


class Server(models.Model):
    ip = models.CharField("管理IP", max_length=15, db_index=True, unique=True, help_text="管理IP")
    hostname = models.CharField("主机名", max_length=15, db_index=True, help_text="主机名")
    cpu = models.CharField("cpu", max_length=50, help_text="cpu")
    mem = models.CharField("mem", max_length=50, help_text="mem")
    disk = models.CharField("disk", max_length=50, help_text="disk", blank=True, null=True)
    os = models.CharField("os", max_length=50, help_text="os", blank=True, null=True)
    sn = models.CharField("sn", max_length=50, help_text="sn", unique=True)
    model_name = models.ForeignKey(ProductModel, verbose_name="服务器型号", help_text="服务器型号")
    manufacturer = models.ForeignKey(Manufacturer, verbose_name="厂商", help_text="厂商", default=1)
    rmt_card_ip = models.CharField("远程管理卡IP", unique=True, max_length=15, help_text="远程管理卡IP", blank=True, null=True)
    cabinet = models.ForeignKey(Cabinet, verbose_name="所在机柜", blank=True, null=True)
    cabinet_position = models.CharField("机柜内位置", max_length=20, blank=True, null=True, help_text="机柜内位置")
    uuid = models.CharField("uuid", max_length=50, db_index=True, unique=True)
    last_check = models.DateField("检测时间", help_text="检测时间", auto_now=True)
    remark = models.TextField('备注', help_text='备注', null=True, blank=True)

    def __str__(self):
        return self.ip

    class Meta:
        db_table = "resource_server"
        ordering = ["id"]
        permissions = (
            ("view_server", "can view server"),
        )


class NetworkDeviceModel(models.Model):
    """
    网卡模型
    """
    name = models.CharField('网卡设备', max_length=20, help_text='网卡设备')
    mac_address = models.CharField('Mac_address', max_length=30, help_text='Mac_address')
    host = models.ForeignKey(Server,verbose_name="所在服务器", help_text='所在服务器')
    remark = models.TextField('备注', help_text='备注', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'resource_network_device'
        ordering = ['id']
        permissions = (
            ("view_networkDevice", "can view networkDevice"),
        )


class IPModel(models.Model):
    """
    IP 模型
    """
    ip_addr = models.CharField("ip地址", max_length=30, db_index=True)
    netmask = models.CharField("子网掩码", max_length=15)
    device = models.ForeignKey(NetworkDeviceModel, verbose_name='所在网卡', help_text='所在网卡')
    remark = models.TextField('备注', help_text='备注', null=True, blank=True)

    class Meta:
        permissions = (
            ("view_IP", "can view IP"),
        )
