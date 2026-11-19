from django.urls import path
from . import views

app_name = 'payment'

urlpatterns = [
    path('listar/', views.list_payments, name='list_payments'),
    path('adicionar/', views.add_payment, name='add_payment'),
]