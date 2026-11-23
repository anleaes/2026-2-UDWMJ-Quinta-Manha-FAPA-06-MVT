from django.urls import path
from . import views

app_name = 'plan'

urlpatterns = [
    path('listar/', views.list_plans, name='list_plans'),
    path('adicionar/', views.add_plan, name='add_plan'),
    path('editar/<int:id_plan>/', views.edit_plan, name='edit_plan'),
    path('excluir/<int:id_plan>/', views.delete_plan, name='delete_plan'),
]