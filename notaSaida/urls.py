from django.urls import path
from .views import *


app_name = 'notaSaida'

urlpatterns = [
    path('notasaida_list/', nota_saida_list, name='saida_list'),
    path('notasaida_new/', nota_saida_new, name="saida_new"),
    path('notasaida_update/<int:pk>/', nota_saida_update, name='saida_update'),
    path('notasaida_delete/<int:pk>/', nota_saida_delete, name='saida_delete')
]