from django.contrib import admin

from shop.models import Category, Product
from django.contrib import admin

# Register your models here.

class CatagoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name','slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category,CatagoryAdmin )


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name','slug','price',]
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Product, ProductAdmin)
