from django.urls import path
from . import views

app_name = 'classbooking'

urlpatterns = [
    path('listar/', views.list_class_bookings, name='list_class_bookings'),
    path('adicionar/', views.add_class_booking, name='add_class_booking'),
    
    
]