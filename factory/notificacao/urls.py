from django.urls import path
from .views import enviar_notificacao

urlpatterns = [
    path('enviar/', enviar_notificacao, name='enviar_notificacao'),
]