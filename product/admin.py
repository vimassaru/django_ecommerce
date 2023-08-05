from django.contrib import admin
from . import models


class VariationInLine(admin.TabularInline):
    model = models.Variation
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'product_name',
                    'get_formatted_price', 'get_formatted_off_price']
    list_display_links = 'id', 'product_name'
    inlines = [
        VariationInLine
    ]


admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.Variation)
