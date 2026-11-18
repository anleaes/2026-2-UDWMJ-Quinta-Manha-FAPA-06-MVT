from django.urls import path
from . import views

app_name = 'contract'

urlpatterns = [
   path('listar/', views.list_contracts, name='list_contracts'),
]