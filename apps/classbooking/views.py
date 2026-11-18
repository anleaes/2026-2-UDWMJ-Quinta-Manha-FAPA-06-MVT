from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import ClassBookingForm
from .models import ClassBooking


@login_required(login_url='/contas/login/')
def list_class_bookings(request):
    template_name = 'classbooking/list_class_bookings.html'
    bookings = ClassBooking.objects.all()
    context = {
        'bookings': bookings,
    }
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def add_class_booking(request):
    template_name = 'classbooking/add_class_booking.html'
    if request.method == 'POST':
        form = ClassBookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('classbooking:list_class_bookings')
    else:
        form = ClassBookingForm()
    context = {
        'form': form,
    }
    return render(request, template_name, context)