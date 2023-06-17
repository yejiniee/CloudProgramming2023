from django.contrib import admin
from .models import Order


class OrderAdmin(admin.ModelAdmin):
    list_display = ('fcuser', 'product', 'quantity',)


admin.site.register(Order, OrderAdmin)
#admin.site.register(Order)