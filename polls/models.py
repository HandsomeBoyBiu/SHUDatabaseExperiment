from django.db import models

# Create your models here.


class Clients(models.Model):
    PROPERTY_CHOICES = [
        ('1', '单位'),
        ('2', '个人'),
        ('3', '未指定')
    ]
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=16)
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
    id = models.IntegerField(primary_key=True)
    date = models.DateField()
