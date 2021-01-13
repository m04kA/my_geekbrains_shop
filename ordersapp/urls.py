from django.urls import  path

import ordersapp.views as ordersapp
from ordersapp.apps import OrdersappConfig

app_name = OrdersappConfig.name

urlpatterns = [
    path("", ordersapp.OrederListView.as_view(), name="orders_list"),
    path("create/", ordersapp.OrederCreateView.as_view(), name="order_create"),
    path("read/<int:pk>/", ordersapp.OrderDetailView.as_view(), name="order_read"),
    path("edit/<int:pk>/", ordersapp.OrederUpdateView.as_view(), name="order_update"),
    path("delete/<int:pk>/", ordersapp.OrderDeleteView.as_view(), name="order_delete"),
    path("complete/<int:pk>/", ordersapp.order_forming_complete, name="order_forming_complete"),
]