from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .forms import NameForm
from django.http import HttpResponseRedirect
# Create your views here.


def index(request):
    template = loader.get_template('../polls/templates/polls/index.html')
    return HttpResponse(template.render(request))


def car(request):
    print('cars')
    print(request.body)
    if request.method == 'POST':
        return car_post(request)   
    elif request.method == 'GET':
        return car_get(request)
    return HttpResponse('car')


def car_post(request):
    form = NameForm(request.POST)
    print(form)
    if form.is_valid():
        # sql语句
        return HttpResponse.http.OK
    

def car_get(request):
    form = NameForm(request.GET)
    print(form)
    if form.is_valid():
        # sql语句
        return HttpResponse.http.OK
    
    
            