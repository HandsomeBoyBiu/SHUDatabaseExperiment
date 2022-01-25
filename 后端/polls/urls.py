from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('car', views.reg_car, name='reg_car'),
    path('client', views.branch_client, name='branch_client'),      # client分支
    path('fix', views.branch_fix, name='branch_fix'),               # fix分支
    path('job', views.repair_order, name='repair_order'),
    path('cars', views.get_all_cars, name="get_all_cars"),
]
