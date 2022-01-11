from django.db import models

# Create your models here.


class Clients(models.Model):
    clientId = models.IntegerField(primary_key=True)
    clientName = models.CharField(max_length=16)
    property = models.CharField(
        max_length=255,
        default='3'
    )
    linkman = models.CharField(max_length=8)
    tele = models.CharField(max_length=11)


class Cars(models.Model):
    licensePlate = models.CharField(primary_key=True)
    color = models.CharField(max_length=4)
    brand = models.CharField(max_length=8)
    type = models.CharField(
        max_length=255,
        default='7'
    )
    belonging = models.CharField(max_length=16)


class FixTables(models.Model):  
    fixTableId = models.IntegerField(primary_key=True)
    registerDate = models.DateField()
    licensePlate = models.CharField()
    fixType = models.CharField(
        max_length=255,
        # choices=FIX_TYPE_CHOICES,
        default='1'
    )
    taskType = models.CharField(
        max_length=255,
        # choices=TASK_TYPE_CHOICES,
        default='2'
    )
    settlementMethods = models.CharField(
        max_length=255
        # choices=SETTLEMENT_METHODS_CHOICES,
    )
    enterTime = models.DateTimeField()
    salesman = models.CharField(max_length=8)
    salesmanId = models.IntegerField()
    predictFinDate = models.DateField()


class MaintenanceMan(models.Model):
    maintenanceManId = models.IntegerField()
    workType = models.CharField(
        max_length=255
        # choices=WORK_TYPE_CHOICES
    )
    unitPrice = models.IntegerField()

# 还差项目表和连接表

class ProjectTable(models.Model):
    projectTableId = models.IntegerField()
    projectType = models.CharField(
        max_length=255
    )
    workTime=models.IntegerField()

# 连接表

class JoinTables(models.Model):
    jointableId=models.IntegerField()
    maintenanceManId = models.IntegerField()
    numbering= models.IntegerField()
    workTime=models.CharField()
