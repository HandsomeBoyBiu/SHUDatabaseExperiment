from django.db import models


# Create your models here.


class Clients(models.Model):
    client_id = models.AutoField(primary_key=True)  # 客户id
    client_name = models.CharField(max_length=16)  # 客户名称
    client_type = models.CharField(  # 客户类型
        max_length=255,
    )
    discount = models.IntegerField()  # 折扣率
    contact = models.CharField(max_length=8)  # 联系人
    tel = models.CharField(max_length=11)  # 电话


class Cars(models.Model):
    car_id = models.CharField(primary_key=True, max_length=16)  # 车辆id
    car_color = models.CharField(max_length=4)  # 车辆颜色
    car_series = models.CharField(max_length=8)  # 车型
    car_type = models.CharField(  # 类型
        max_length=255,
    )
    belonging = models.CharField(max_length=16, default='None')  # 车辆所属人


class FixTables(models.Model):
    fix_id = models.AutoField(primary_key=True)  # 维修表id
    register_time = models.DateField(auto_now_add=True)  # 注册时间
    car_id = models.CharField(max_length=16)  # 车牌号
    priority = models.CharField(  # 维修类型（普通）
        max_length=255,
    )
    fix_type = models.CharField(  # 作业类型（中修）
        max_length=255,
    )
    pay = models.CharField(  # 结算方式
        max_length=255
    )
    in_time = models.DateTimeField()  # 进厂时间
    clerk_name = models.CharField(max_length=8)  # 业务员姓名
    clerk_id = models.IntegerField()  # 业务员id
    est_time = models.DateTimeField()  # 预计完工时间
    describe = models.CharField(max_length=255, null=True)  # 故障描述


# 维修工表
class FixMan(models.Model):
    fix_man_id = models.AutoField(primary_key=True)  # 维修员id
    work_type = models.CharField(  # 工种
        max_length=255
    )
    unit_price = models.IntegerField()  # 单价


# 项目表
class ProjectTable(models.Model):
    project_table_id = models.AutoField(primary_key=True)  # 项目表id
    project_type = models.CharField(  # 项目类型
        max_length=255
    )


# 连接表
class JoinTables(models.Model):
    # 前三个参数用于连接前三张表
    fix_id = models.IntegerField(null=True)  # 维修表id
    fix_man_id = models.IntegerField(null=True)  # 维修员id
    project_table_id = models.IntegerField(null=True)  # 项目表id
    work_time = models.IntegerField(null=True)  # 工作时长
    status = models.BooleanField(default=False)                  # 表单状态（已完成/未完成）
