from django.urls import path
from .views import entrada_list, entrada_new

app_name = 'entrada'

urlpatterns = [
    path('entrada_list/', entrada_list, name='entrada_list'),
    path('entrada_new/', entrada_new, name='entrada_new'),
]
