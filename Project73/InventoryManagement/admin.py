from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display=['Date','Provider','Name_of_product','Price','Quantity','Amount','Stock']
admin.site.register( Product,ProductAdmin)    