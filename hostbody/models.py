# coding=utf-8
from __future__ import unicode_literals

from django.db import models
from hostbody.custom_auth import UserProfile

# Create your models here.


class HostInfo(models.Model):
    instance_id = models.CharField(u'实例ID', max_length=32, unique=True)
    custom_name = models.CharField(u'自定义名称', max_length=32)
    region = models.CharField(u'Region名称', max_length=32)
    region_part = models.CharField(u'所在可用区', max_length=32)
    ip_public = models.GenericIPAddressField(u'公网IP', max_length=32, unique=True)
    ip_private = models.GenericIPAddressField(u'内网IP', max_length=32, unique=True)
    cpu_num = models.IntegerField(u'CPU', )
    memory = models.IntegerField(u'内存', )
    pay_type = models.CharField(u'付费类型', max_length=32)
    net_type = models.CharField(u'网络类型', max_length=32)
    bandwidth = models.IntegerField(u'带宽', )
    remark = models.TextField(u'标签', max_length=1024, default='Null')
    creation_time = models.CharField(u'创建时间', max_length=32)
    expired_time = models.CharField(u'过期时间', max_length=32)
    # group = models.ManyToManyField('GroupInfo', blank=True)
    # user = models.ManyToManyField('UserProfile', blank=True)

    def __unicode__(self):
        return self.custom_name


class GroupInfo(models.Model):
    group_name = models.CharField(max_length=32, unique=True)
    remark = models.TextField(max_length=1024, default='Null')
    user = models.ManyToManyField("UserProfile", blank=True)
    host = models.ManyToManyField('HostInfo', blank=True)

    def __unicode__(self):
        return self.group_name
