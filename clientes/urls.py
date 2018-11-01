from django.urls import path, include
from .views import hello, clientes_list, clientes_new, clientes_update, clientes_delete

urlpatterns = [
    path('hello/', hello),
    path('list/', clientes_list, name='clientes_list'),
    path('new/', clientes_new, name='clientes_new'),
    path('update/<int:id>', clientes_update, name='clientes_update'),
    path('delete/<int:id>', clientes_delete, name='clientes_delete'),


]