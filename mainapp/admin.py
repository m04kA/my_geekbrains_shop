from django.contrib import admin

from .models import Product, ProductCategory, Contact

admin.site.register(ProductCategory)
admin.site.register(Product)
admin.site.register(Contact)