from django.urls import path
from . import views

app_name = 'modality'

urlpatterns = [
    path('listar/', views.list_modalities, name='list_modalities'),
    path('adicionar/', views.add_modality, name='add_modality'),
    path('editar/<int:id_modality>/', views.edit_modality, name='edit_modality'),
    path('excluir/<int:id_modality>/', views.delete_modality, name='delete_modality'),
]