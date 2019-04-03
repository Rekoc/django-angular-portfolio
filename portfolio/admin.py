from django.contrib import admin
from portfolio.models import PortfolioItem, ImageField


class PortfolioItemAdmin(admin.ModelAdmin):
    pass


class ImageFieldAdmin(admin.ModelAdmin):
    pass


admin.site.register(ImageField, ImageFieldAdmin)
admin.site.register(PortfolioItem, PortfolioItemAdmin)

