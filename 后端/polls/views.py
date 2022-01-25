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


def index(request):
    template = loader.get_template('../polls/templates/polls/index.html')
    return HttpResponse(template.render(request))


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


# 由于派工单需要两种请求方式，因此这里写了一个分支
def repair_order(request):
    print("### [Branch] repair_order ###")
    if request.method == 'GET':
        return get_tickets(request)
    elif request.method == 'POST':
        return post_repair_order(request)


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
        JoinTables(fix_id=para, fix_man_id=d['worker_id'], project_table_id=d['job_id'], work_time=d['time']).save()
    response = HttpResponse()
    response.status_code = 200
    return response


# def car_post(request):
# form = NameForm(request.POST)
# print(form)
# if form.is_valid():
#     # sql语句
#     return HttpResponse.http.OK


# def car_get(request):
# form = NameForm(request.GET)
# print(form)
# if form.is_valid():
#     # sql语句
#     return HttpResponse.http.OK

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
        ls = {'job_id': ticket.project_table_id,
              'fix_name': list(ProjectTable.objects.filter(project_table_id=ticket.project_table_id))[0].project_type,
              'time': ticket.work_time, 'work_id': ticket.fix_man_id,
              'worker_name': list(FixMan.objects.filter(fix_man_id=ticket.fix_man_id))[0].work_type}
        jsonlist.append(ls)
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
    ls = list(clients)
    print(ls)
    # custom = clients[0]
    for custom in clients:
        qs1 = Cars.objects.filter(belonging=custom['client_id']).values_list('car_id', "car_color", "car_series",
                                                                             "car_type")
        custom['cars'] = car_exchange(qs1, custom['client_id'])
    # cars = Cars.objects.filter(belonging=1)
    # cars.query = pickle.loads((pickle.dumps(qs1.query)))
    # print(list(cars))
    # data = serializers.serialize("json", client)
    # print(clients)
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
        fix_table['client_id'] = list(Cars.objects.filter(car_id=fix_table['car_id']))[0].belonging
    print(ls)
    return HttpResponse(json.dumps(ls, ensure_ascii=False, cls=ComplexEncoder))


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
