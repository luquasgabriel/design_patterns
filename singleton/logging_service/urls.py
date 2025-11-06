from django.urls import path
from .views import logs_recentes

urlpatterns = [
    path('recentes/', logs_recentes, name='logs_recentes'),
]
