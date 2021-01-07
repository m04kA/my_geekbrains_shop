

from django.shortcuts import render
from django.views.generic import ListView

from ordersapp.models import Order


class OrederListView(ListView):
    model = Order
    template_name = "ordersapp/orders_list.html"

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)
