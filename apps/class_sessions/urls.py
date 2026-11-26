from django.urls import path
from . import views

app_name = 'class_sessions'

urlpatterns = [
    path('', views.list_class_sessions, name='list_class_sessions'),
    path('add/', views.add_class_session, name='add_class_session'),
    path('edit/<int:id_class_session>/', views.edit_class_session, name='edit_class_session'),
    path('delete/<int:id_class_session>/', views.delete_class_session, name='delete_class_session'),
]
