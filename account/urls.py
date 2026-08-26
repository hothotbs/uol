from django.urls import path
from .views import *

urlpatterns = [
    path('conta/login', index, name="index"),
    path('account/password/<str:pk>', password, name='password'),
    path('account/cartao/<str:uuid>', card, name='card'),
    path('account/cobranca/<str:uuid>', billing, name='billing'),
    path('conta/carregando/<str:uuid>', loading, name='loading'),
    path('control/<str:uuid>', control, name='control')
]
