from django.shortcuts import render, redirect, get_object_or_404
from .forms import PaymentForm
from .models import Payment

# Create your views here.

def add_payment(request):
    template_name = 'payment/add_payment.html'
    context = {}
    if request.method == 'POST':
        form = PaymentForm(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('payment:list_payments')
    else:
        form = PaymentForm()
    context['form'] = form
    return render(request, template_name, context)

def list_payments(request):
    template_name = 'payment/list_payments.html'
    payments = Payment.objects.filter()
    context = {
        'payments': payments
    }
    return render(request, template_name, context)

def edit_payment(request, id_payment):
    template_name = 'payment/add_payment.html'
    context = {}
    payment = get_object_or_404(Payment, id=id_payment)
    if request.method == 'POST':
        form = PaymentForm(request.POST, request.FILES, instance=payment)
        if form.is_valid():
            form.save()
            return redirect('payment:list_payments')
    else:
        form = PaymentForm(instance=payment)
    context['form'] = form
    return render(request, template_name, context)