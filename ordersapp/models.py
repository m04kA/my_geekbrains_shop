from django.conf import settings
from django.db import models

from mainapp.models import Product


class Order(models.Model):
    FORMING = "FM"
    SEND_TO_PROCEED = "STP"
    PROCEED = "PRD"
    PAID = "PD"
    READY = "PDY"
    CHANCEL = "CNC"
    ORDER_STATUS = (
        (FORMING, "Формируется"),
        (SEND_TO_PROCEED, "Отправлен на обработку"),
        (PROCEED, "Обработан"),
        (PAID, "Оплачен"),
        (READY, "Готов к выдаче"),
        (CHANCEL, "Отменено")
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="пользователь")
    status = models.CharField(max_length=3, choices=ORDER_STATUS, default=FORMING, verbose_name="статус")
    is_active = models.BooleanField(default=True, verbose_name="активен")
    created = models.DateTimeField(auto_now_add=True, verbose_name="дата создания заказа")
    updated = models.DateTimeField(auto_now=True, verbose_name="дата обновления заказа")

    def get_total_quantity(self):
        "return total quantity for user"
        _items = self.orderitems.select_related()
        _totalquantity = sum(list(map(lambda x: x.quantity, _items)))
        return _totalquantity

    def get_total_cost(self):
        "return total cost for user"
        _items = self.orderitems.select_related()
        _totalcost = sum(list(map(lambda x: x.product_cost, _items)))
        return _totalcost


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name="Заказ", related_name="orderitems")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Продукт")
    quantity = models.PositiveIntegerField(default=0, verbose_name="Количество")

    @property
    def product_cost(self):
        "return cost of all products this type"
        return self.product.price * self.quantity

    @staticmethod
    def get_item(pk):
        return OrderItem.objects.get(pk=pk)
