from django.urls import path
from . import views

app_name = 'assessment'

urlpatterns = [
    path('listar/', views.list_assessments, name='list_assessments'),
    path('adicionar/', views.add_assessment, name='add_assessment'),
    path('editar/<int:id_assessment>/', views.edit_assessment, name='edit_assessment'),
    path('excluir/<int:id_assessment>/', views.delete_assessment, name='delete_assessment'),
]