from django.contrib import admin

from .models import PromoCode

class PromoCodeAdmin(admin.ModelAdmin):
    exclude = ['code']

admin.site.register(PromoCode, PromoCodeAdmin)
