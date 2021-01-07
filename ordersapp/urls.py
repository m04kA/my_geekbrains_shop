from django.urls import  path

import ordersapp.views as ordersapp
from ordersapp.apps import OrdersappConfig

app_name = OrdersappConfig.name

urlpatterns = [
    path("", ordersapp.OrederListView.as_view(), name="orders_list"),
]