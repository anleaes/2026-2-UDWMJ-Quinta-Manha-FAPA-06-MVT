from django.urls import path
from . import views

app_name = 'assessment'

urlpatterns = [
    path('listar/', views.list_assessments, name='list_assessments'),

]