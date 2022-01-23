from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from polls.models import *
import json
# from .forms import NameForm
from django.http import HttpResponseRedirect
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
    m_cars = Cars(car_id=data['car_id'], car_color=data['car_color'], car_series=data['car_series'], car_type=data['car_type'])
    m_cars.save()
    response = HttpResponse()
    response.status_code = 200
    return response


# 测试成功
def reg_client(request):
    print('### [Request POST] reg_client ###')
    data = json.loads(request.body.decode('utf-8'))
    print(data)
    # 这里需要动两张表
    # 1、客户表添加客户
    clients = Clients(client_name=data['client_name'], client_type=data['client_type'], discount=data['discount'], contact=data['contact'], tel=data['tel'])
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
    fixtable = FixTables(car_id=data['car_id'], priority=data['priority'], fix_type=data['type'], pay=data['pay'], in_time=data['in_time'], clerk_name=data['clerk_name'], clerk_id=data['clerk_id'], est_time=data['est_time'], describe=data['describe'])
    fixtable.save()
    response = HttpResponse()
    response.status_code = 500
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


def client(request):
    return HttpResponse.http.OK
    
    
            