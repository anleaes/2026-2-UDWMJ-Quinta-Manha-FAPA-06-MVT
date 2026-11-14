from django.urls import path

from . import views

app_name = 'member'

urlpatterns = [
    path('listar/', views.list_members, name='list_members'),
    path('adicionar/', views.add_member, name='add_member'),
    path('editar/<int:id_member>/', views.edit_member, name='edit_member'),
    path('excluir/<int:id_member>/', views.delete_member, name='delete_member'),
 
]