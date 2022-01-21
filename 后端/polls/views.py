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


def car(request):
    print('### [Request POST] car ###')
    # json转dict
    data = json.loads(request.body.decode("utf-8"))
    # 请求体数据: {"car_id":"id","car_color":"color","car_series":"123","car_type":"轿车"}
    # 数据库插入
    m_cars = Cars(car_id=data['car_id'], car_color=data['car_color'], car_series=data['car_series'], car_type=data['car_type'])
    m_cars.save()
    response = HttpResponse()
    response.status_code = 200
    return response
    # if request.method == 'POST':
    #     return car_post(request)
    # elif request.method == 'GET':
    #     return car_get(request)
    # return HttpResponse('car')


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
    
    
            