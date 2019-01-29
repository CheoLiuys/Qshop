from django.urls import path,re_path
from Buyer.views import *

urlpatterns = [
    re_path('^$', index),
    path('index/', index),
    path('sendMail/', sendMessage),
    re_path('goods_details/(?P<id>\d+)/', goods_details),
    re_path('carJump/(?P<goods_id>\d+)/', carJump),
    path('carList/', carList),
    re_path('delete_goods/(?P<goods_id>\d+)', delete_goods),
    path('clear_goods/', clear_goods),
    path('enter_order/', add_order),
    path('address/', address),
    path('addAddress/', addAddress),
    re_path('changeAddress/(?P<address_id>\d+)/', changeAddress),
    re_path('delAddress/(?P<address_id>\d+)/', delAddress),
]