from django.urls import path
from .views import entrada_list, entrada_new, entrada_update, entrada_delete

app_name = 'entrada'

urlpatterns = [
    path('entrada_list/', entrada_list, name='entrada_list'),
    path('entrada_new/', entrada_new, name='entrada_new'),
    path('entrada_update/<int:pk>/', entrada_update, name='entrada_update'),
    path('entrada_delete/<int:pk>/', entrada_delete, name='entrada_delete')
]
