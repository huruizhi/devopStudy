from django.db import models

# Create your models here.


class Manufacturer(models.Model):
    vendor_name = models.CharField("厂商名称", max_length=32, db_index=True, unique=True)
    tel = models.CharField("联系电话", max_length=15, null=True, blank=True)
    mail = models.CharField('邮箱地址', null=True, blank=True)

