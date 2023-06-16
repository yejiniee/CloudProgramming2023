from django.contrib import admin
from .models import Product, ProductCategory

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price',)

admin.site.register(Product, ProductAdmin)

class ProductCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}

admin.site.register(ProductCategory, ProductCategoryAdmin)