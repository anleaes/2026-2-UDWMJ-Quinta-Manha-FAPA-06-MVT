from django.urls import path

from . import views

app_name = 'employee'

urlpatterns = [
    path('listar/', views.list_employees, name='list_employees'),
]