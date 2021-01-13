from django.db import transaction
from django.forms import inlineformset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from basketapp.models import Basket
from ordersapp.forms import OrderItemForm
from ordersapp.models import Order, OrderItem


class OrederListView(ListView):
    model = Order
    template_name = "ordersapp/orders_list.html"

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)


class OrederCreateView(CreateView):
    model = Order
    fields = []
    success_url = reverse_lazy("ordersapp:orders_list")  # ordersapp:order_update
    template_name = "ordersapp/order_form.html"

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        OrderFormSet = inlineformset_factory(Order, OrderItem, form=OrderItemForm, extra=1)
        if self.request.POST:
            formset = OrderFormSet(self.request.POST)
        else:
            busket_items = Basket.objects.filter(user=self.request.user)
            if len(busket_items):
                OrderFormSet = inlineformset_factory(Order, OrderItem, form=OrderItemForm, extra=len(busket_items))
                formset = OrderFormSet()
                for num, form in enumerate(formset.forms):
                    form.initial['product'] = busket_items[num].product
                    form.initial['quantity'] = busket_items[num].quantity
                busket_items.delete()
            else:
                formset = OrderFormSet()
        data['orderitems'] = formset

        return data

    def form_valid(self, form):
        context = self.get_context_data()
        orderitems = context['orderitems']

        with transaction.atomic():
            form.instance.user = self.request.user
            self.object = form.save()
            if orderitems.is_valid():
                orderitems.instance = self.object
                orderitems.save()
        if self.object.get_total_cost() == 0:
            self.object.delete()

        return super().form_valid(form)


class OrederUpdateView(UpdateView):
    model = Order
    fields = []
    success_url = reverse_lazy("ordersapp:orders_list")
    template_name = "ordersapp/order_form.html"

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        OrderFormSet = inlineformset_factory(Order, OrderItem, form=OrderItemForm, extra=1)
        if self.request.POST:
            formset = OrderFormSet(self.request.POST, instance=self.object)
        else:
            formset = OrderFormSet(instance=self.object)
        data['orderitems'] = formset

        return data

    def form_valid(self, form):
        context = self.get_context_data()
        orderitems = context['orderitems']

        with transaction.atomic():
            self.object = form.save()
            if orderitems.is_valid():
                orderitems.instance = self.object
                orderitems.save()

        return super().form_valid(form)


class OrderDetailView(DetailView):
    model = Order


class OrderDeleteView(DeleteView):
    model = Order
    success_url = reverse_lazy("ordersapp:orders_list")


def order_forming_complete(requesr, pk):
    order = get_object_or_404(Order, pk=pk)
    order.status = Order.SEND_TO_PROCEED
    order.save()
    return HttpResponseRedirect(reverse("ordersapp:orders_list"))
