from django.urls import path
from . import views

app_name = 'contract'

urlpatterns = [
   path('listar/', views.list_contracts, name='list_contracts'),
   path('adicionar/', views.add_contract, name='add_contract'),
   path('editar/<int:id_contract>/', views.edit_contract, name='edit_contract'),
   path('excluir/<int:id_contract>/', views.delete_contract, name='delete_contract'),
]