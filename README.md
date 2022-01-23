# 上海大学数据库原理课程项目
## 车辆维修管理系统
### 前端：lzp 后端：wyw，wb

### 已知问题

1. 在客户登记中，车牌号为选择框，选择框中的车牌数据哪里来？同样的问题也存在于维修委托登记中，是否需要后端新增选择框的数据接口？
2. 维修委托登记前端没有数据传过来

### 后端常用命令

对应用polls进行数据库迁移，可以理解为生成sql语句但不执行，其中，生成的“sql语句”存放于该应用目录下的migrations文件夹下。

```shell
python manage.py makemigrations polls
```

进行数据库迁移，可以理解为执行前面生成的sql语句

```
python manage.py migrate
```

数据表结构（*表示该属性仅在后端出现）（%表示前后端属性名不同，%前为前端的属性名，%后为后端的属性名）

1、客户表

| 客户名称    | 客户id    | 性质        | 联系人  | 电话 | 折扣率   |
| ----------- | --------- | ----------- | ------- | ---- | -------- |
| client_name | client_id | client_type | contact | tel  | discount |

2、车辆表

| 车牌号 | 车辆颜色  | 车型       | 类型     | 所属人（客户id） |
| ------ | --------- | ---------- | -------- | ---------------- |
| car_id | car_color | car_series | car_type | *belonging       |

3、维修表

| 维修表ID | 注册时间       | 车牌号 | 维修类型 | 作业类型      |
| -------- | -------------- | ------ | -------- | ------------- |
| fix_id   | *register_time | car_id | priority | type%fix_type |

| 结算方式 | 进厂时间 | 业务员姓名 | 业务员id | 预计完工时间 | 故障描述 |
| -------- | -------- | ---------- | -------- | ------------ | -------- |
| pay      | in_time  | clerk_name | clerk_id | est_time     | describe |

4、维修工表

| 维修员id             | 工种                  | 单价        |
| -------------------- | --------------------- | ----------- |
| worker_id%fix_man_id | worker_name%work_type | *unit_price |

5、项目表

| 项目表id                | 项目类型              |
| ----------------------- | --------------------- |
| job_id%project_table_id | fix_name%project_type |

6、连接表

| 维修表id | 维修员id             | 项目表id                | 工作时长       |
| -------- | -------------------- | ----------------------- | -------------- |
| fix_id   | worker_id%fix_man_id | job_id%project_table_id | time%work_time |

### 2022-1-4
* 新建项目
* 导入前端框架
* 创建部分数据表


### 2022-1-11
* 对后端models.py进行添加
* 对views中增加car的get和post大致框架（form是获取json内容，通过键值对取值）
* 前后端对于car测试通过

### 2022-1-21

* 完善数据库属性名
* 将models迁移至数据库（sqlite），完成数据表的创建
* 部分数据表框架写入README.md

### 2022-1-21晚

* 所有数据表框架写入README.md，实现前后端属性名映射

### 2022-1-23

* 完善部分数据表的数据存储方式
* 新增reg_client和reg_fix_table接口，后者没有测试过，前者测试通过
* 转为使用mysql数据库（***注意：./后端/djangoProject/setting.py中需要将密码改成自己mysql的密码，数据库名为vrsms(Vehicle Repair Service Management System)***）