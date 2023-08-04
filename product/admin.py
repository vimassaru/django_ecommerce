from django.contrib import admin
from . import models


class VariationInLine(admin.TabularInline):
    model = models.Variation
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    inlines = [
        VariationInLine
    ]


admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.Variation)
