from django.db import models

# Create your models here.


class Clients(models.Model):
    PROPERTY_CHOICES = [
        ('1', '单位'),
        ('2', '个人'),
        ('3', '未指定')
    ]
    clientId = models.IntegerField(primary_key=True)
    clientName = models.CharField(max_length=16)
    property = models.CharField(
        max_length=1,
        choices=PROPERTY_CHOICES,
        default='3'
    )
    linkman = models.CharField(max_length=8)
    tele = models.CharField(max_length=11)


class Cars(models.Model):
    TYPE_CHOICES = [
        ('1', '轿车'),
        ('2', 'SUV'),
        ('3', 'MPV'),
        ('4', '跑车'),
        ('5', '皮卡'),
        ('6', '其他'),
        ('7', '未指定')
    ]
    licensePlate = models.CharField(primary_key=True)
    color = models.CharField(max_length=4)
    brand = models.CharField(max_length=8)
    type = models.CharField(
        max_length=1,
        choices=TYPE_CHOICES,
        default='7'
    )
    belonging = models.CharField(max_length=16)


class FixTables(models.Model):
    FIX_TYPE_CHOICES = [
        ('1', '维护'),
        ('2', '修理')
    ]
    TASK_TYPE_CHOICES = [
        ('1', '维护'),
        ('2', '轻度修理'),
        ('3', '中度修理'),
        ('4', '重度修理')
    ]
    # From: https://zhuanlan.zhihu.com/p/163411392
    SETTLEMENT_METHODS_CHOICES = [
        ('1', '自费'),
        ('2', '自负'),
        ('3', '分类自负'),
        ('4', '自付'),
    ]
    fixTableId = models.IntegerField(primary_key=True)
    registerDate = models.DateField()
    licensePlate = models.CharField()
    fixType = models.CharField(
        max_length=1,
        choices=FIX_TYPE_CHOICES,
        default='1'
    )
    taskType = models.CharField(
        max_length=1,
        choices=TASK_TYPE_CHOICES,
        default='2'
    )
    settlementMethods = models.CharField(
        max_length=1,
        choices=SETTLEMENT_METHODS_CHOICES,
    )
    enterTime = models.DateTimeField()
    salesman = models.CharField(max_length=8)
    salesmanId = models.IntegerField()
    predictFinDate = models.DateField()


class MaintenanceMan(models.Model):
    WORK_TYPE_CHOICES = [
        ('1', '机修'),
        ('2', '漆工'),
        ('3', '焊工')
    ]
    maintenanceManId = models.IntegerField()
    workType = models.CharField(
        max_length=1,
        choices=WORK_TYPE_CHOICES
    )
    unitPrice = models.IntegerField()

# 还差项目表和连接表
