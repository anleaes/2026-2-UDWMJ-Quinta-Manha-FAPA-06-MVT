from django.urls import path

from . import views

app_name = 'member'

urlpatterns = [
    path('listar/', views.list_members, name='list_members'),
 
]