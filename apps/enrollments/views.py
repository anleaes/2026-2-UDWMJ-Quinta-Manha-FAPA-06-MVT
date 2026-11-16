from django.shortcuts import render
from .forms import EnrollmentForm
from .models import Enrollment

# Create your views here.

def add_enrollment(request):
    template_name = 'enrollment/add_enrollment.html'
    context = {}
    if request.method == 'POST':
        form = EnrollmentForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('enrollment:list_enrollments')
    else:
        form = EnrollmentForm()
    context['form'] = form
    return render(request, template_name, context)