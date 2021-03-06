from django.http import HttpResponse
from django.template import loader
from .models import *
import json
from django.core import serializers
from django.core import serializers
from django.http import HttpResponseRedirect
import pickle
from datetime import date, datetime


# Create your views here.


# 测试成功
def reg_car(request):
    print('### [Request POST] reg_car ###')
    # json转dict
    data = json.loads(request.body.decode("utf-8"))
    # 请求体数据: {"car_id":"id","car_color":"color","car_series":"123","car_type":"轿车"}
    # 数据库插入
    m_cars = Cars(car_id=data['car_id'], car_color=data['car_color'], car_series=data['car_series'],
                  car_type=data['car_type'])
    m_cars.save()
    response = HttpResponse()
    response.status_code = 200
    return response


# client分支结构，分别处理POST和GET
def branch_client(request):
    if request.method == 'POST':
        return reg_client(request)
    elif request.method == 'GET':
        return get_client(request)


# 测试成功
def reg_client(request):
    print('### [Request POST] reg_client ###')
    data = json.loads(request.body.decode('utf-8'))
    print(data)
    # 这里需要动两张表
    # 1、客户表添加客户
    clients = Clients(client_name=data['client_name'], client_type=data['client_type'], discount=data['discount'],
                      contact=data['contact'], tel=data['tel'])
    clients.save()
    # 2、车辆表添加车辆下的客户名
    car = Cars.objects.get(car_id=data['car_id'])
    car.belonging = data['client_name']
    car.save()
    response = HttpResponse()
    response.status_code = 200
    return response


# 前端没传数据到这里，所以没测试过，但我觉得应该没问题
def reg_fix_table(request):
    print('### [Request POST] reg_fix_table ###')
    data = json.loads(request.body.decode('utf-8'))
    print(data)
    fixtable = FixTables(car_id=data['car_id'], priority=data['priority'], fix_type=data['type'], pay=data['pay'],
                         in_time=data['in_time'], clerk_name=data['clerk_name'], clerk_id=data['clerk_id'],
                         est_time=data['est_time'], describe=data['describe'])
    print(fixtable)
    fixtable.save()
    response = HttpResponse()
    response.status_code = 200
    return response


def branch_fix(request):
    if request.method == 'POST':
        return reg_fix_table(request)
    elif request.method == 'GET':
        return get_fix(request)


# 派工单的post请求
def post_repair_order(request):
    print('### [Request POST] post_repair_order ###')
    # 这里需要两步
    para = request.GET.get('fix_id')  # 获取url中的请求参数
    data = json.loads(request.body.decode('utf-8'))  # 获取POST的数据
    # 1、删除原有数据
    JoinTables.objects.filter(fix_id=para).delete()
    # 2、新增数据
    for d in data:
        fm = FixMan.objects.get(work_type=d['worker_name'])
        jn = ProjectTable.objects.get(project_type=d['job_name'])
        JoinTables(fix_id=para, fix_man_id=fm.fix_man_id, project_table_id=jn.project_table_id,
                   work_time=d['time'], status=d['status']).save()
    response = HttpResponse()
    response.status_code = 200
    return response


# 由于派工单需要两种请求方式，因此这里写了一个分支
def repair_order(request):
    print("### [Branch] repair_order ###")
    if request.method == 'GET':
        return get_tickets(request)
    elif request.method == 'POST':
        return post_repair_order(request)


# 派工单的GET请求
# 查询工单 GET {baseURL}/job?fix_id={fix_id}
# job_id,fix_name,time,work_id,worker_name
# 测试通过
def get_tickets(request):
    print('### [Request GET] get_tickets ###')
    jsonlist = []
    fix_id = request.GET.get("fix_id")
    res = JoinTables.objects.filter(fix_id=fix_id)
    # print(res)
    tickets = list(res)
    for ticket in tickets:
        try:
            ls = {'job_id': ticket.project_table_id,
                  'job_name': list(ProjectTable.objects.filter(project_table_id=ticket.project_table_id))[
                      0].project_type,
                  'time': ticket.work_time, 'worker_id': ticket.fix_man_id,
                  'worker_name': list(FixMan.objects.filter(fix_man_id=ticket.fix_man_id))[0].work_type,
                  'status': ticket.status}
            jsonlist.append(ls)
        except:
            jsonlist.append([])
    return HttpResponse(json.dumps(jsonlist, ensure_ascii=False))


# 获取所有车辆信息 获得数据库中已有的车辆信息 GET {baseURL}/cars
# 测试成功
def get_all_cars(request):
    print('### [Request GET] get_all_cars ###')
    qs = Cars.objects.values_list("car_id", "car_color", "car_series", "car_type", named=True)
    cars = Cars.objects.all()
    cars.query = pickle.loads(pickle.dumps(qs.query))
    ls = list(cars)
    for car in ls:
        car['id'] = car.pop('car_id')
        car['color'] = car.pop('car_color')
        car['series'] = car.pop('car_series')
        car['type'] = car.pop('car_type')
    # print(type(qs))
    return HttpResponse(json.dumps(ls, ensure_ascii=False))


# 获取数据库中客户信息 GET {baseURL}/client ?加入一个cars有问题 暂时不会
def get_client(request):
    print('### [Request GET] get_client ###')
    qs = Clients.objects.values_list("client_id", "client_name", "client_type", "discount", "contact", "tel",
                                     named=True)
    clients = Clients.objects.all()
    clients.query = pickle.loads(pickle.dumps(qs.query))

    # for custom in clients:
    #     car = Cars.objects.get(belonging=custom['client_name'])
    #     custom['cars'] = [{
    #         "id": car.car_id,
    #         "color": car.car_color,
    #         "type": car.car_type
    #     }]
    for custom in clients:
        cars = Cars.objects.filter(belonging=custom['client_name'])
        for car in cars:
            custom['cars'] = [{
                "id": car.car_id,
                "color": car.car_color,
                "type": car.car_type
            }]

    ls = list(clients)
    print(ls)
    return HttpResponse(json.dumps(ls, ensure_ascii=False))


def car_exchange(qs1, num):
    cars = Cars.objects.filter(belonging=num)
    cars.query = pickle.loads(pickle.dumps(qs1.query))
    ls = list(cars)
    for car in ls:
        car['id'] = car.pop('car_id')
        car['color'] = car.pop('car_color')
        car['series'] = car.pop('car_series')
        car['type'] = car.pop('car_type')
    return ls


# 获取维修委托单信息 GET {baseURL}/fix
# 测试成功
def get_fix(request):
    print('### [Request GET] get_fix ###')
    qs = FixTables.objects.values_list("fix_id", "car_id", "priority", "fix_type", "pay", "in_time",
                                       "clerk_name", "clerk_id", "est_time", "describe", named=True)
    fix_tables = FixTables.objects.all()
    fix_tables.query = pickle.loads(pickle.dumps(qs.query))
    ls = list(fix_tables)
    for fix_table in ls:
        # ----------- 测试获取订单状态 -----------
        tmpId = fix_table['fix_id']
        tmpJoinedTable = JoinTables.objects.filter(fix_id=tmpId)
        flag = True
        for table in tmpJoinedTable:
            if not table.status:
                flag = False
                break
        fix_table['status'] = flag
        # ----------- 测试获取订单状态 -----------
        try:
            fix_table['client_id'] = list(Cars.objects.filter(car_id=fix_table['car_id']))[0].belonging
        except:
            fix_table['client_id'] = []
    # print(ls)
    return HttpResponse(json.dumps(ls, ensure_ascii=False, cls=ComplexEncoder))


def get_report(request):
    print('### [Request GET] get_report ###')
    fix_id = request.GET.get('fix_id')
    fix_table = FixTables.objects.get(fix_id=fix_id)
    car = Cars.objects.get(car_id=fix_table.car_id)
    client = Clients.objects.get(client_name=car.belonging)
    ret = {
        "client_name": client.client_name,
        "client_type": client.client_type,
        "discount": client.discount,
        "car_id": car.car_id,
        "priority": fix_table.priority,
        "fix_type": fix_table.fix_type,
        "pay": fix_table.pay,
        "in_time": fix_table.in_time,
        "clerk_name": fix_table.clerk_name,
        "describe": fix_table.describe
    }

    jointables = JoinTables.objects.filter(fix_id=fix_id)
    fixLs = []
    for i in jointables:
        job = ProjectTable.objects.get(project_table_id=i.project_table_id)
        worker = FixMan.objects.get(fix_man_id=i.fix_man_id)
        fixLs.append({
            "job_id": i.project_table_id,
            "job_name": job.project_type,
            "time": i.work_time,
            "worker_id": i.fix_man_id,
            "worker_name": worker.work_type,
            "unit_price": worker.unit_price,
            "subtotal": worker.unit_price * i.work_time
        })
    ret['fix'] = fixLs
    ret['total'] = 0
    for i in fixLs:
        ret['total'] += i['subtotal']

    # zidian = {'fix': abc}
    # lis.append(zidian)
    # prin(ls)
    # print(list(FixMan.object.filter(fix_man_id=fix_table['fix_man_id']))[0].unit_price)
    return HttpResponse(json.dumps(ret, ensure_ascii=False, cls=ComplexEncoder))


class ComplexEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        else:
            return json.JSONEncoder.default(self, obj)


def client(request):
    return HttpResponse.http.OK
