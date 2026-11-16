from django.urls import path
from . import views

app_name = 'enrollment'

urlpatterns = [
    path('listar/', views.list_enrollments, name='list_enrollments'),
    
    ]