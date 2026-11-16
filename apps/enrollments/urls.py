from django.urls import path
from . import views

app_name = 'enrollment'

urlpatterns = [
    path('listar/', views.list_enrollments, name='list_enrollments'),
    path('adicionar/', views.add_enrollment, name='add_enrollment'),
    ]