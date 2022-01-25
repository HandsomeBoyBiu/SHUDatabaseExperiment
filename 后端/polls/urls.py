from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('car/', views.reg_car, name='reg_car'),
    path('client', views.branch_client, name='branch_client'),
    path('fix', views.reg_fix_table, name='reg_fix_table'),
    path('job', views.repair_order, name='repair_order'),
    path('cars', views.get_all_cars, name="get_all_cars"),
    path('fixes', views.get_fix, name="get_fix")
]
