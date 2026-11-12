from django.urls import path

from . import views

app_name = 'person'

urlpatterns = [
    path('listar/', views.list_persons, name='list_persons'),
    path('adicionar/', views.add_person, name='add_person'),
]