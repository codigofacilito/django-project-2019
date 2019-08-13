from django.urls import path

from . import views

app_name = 'promo_codes'

urlpatterns = [
    path('validar', views.validate, name='validate')
]
