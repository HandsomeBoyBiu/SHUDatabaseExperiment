from unicodedata import name
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('car/', views.reg_car, name='reg_car'),
    path('client', views.reg_client, name='reg_client'),
    path('fix', views.reg_fix_table, name='reg_fix_table'),
    path('job',views.views.get_tickets,name='get_tickets')
]
