from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import ClassBookingForm
from .models import ClassBooking

# Create your views here.
