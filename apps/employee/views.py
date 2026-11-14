from django.shortcuts import redirect, render
from .forms import EmployeeForm
from .models import Employee


# Create your views here.
def list_employees(request):
    template_name = 'employee/list_employees.html'
    employees = Employee.objects.filter()
    context = {
        'employees': employees,
    }
    return render(request, template_name, context)
def add_employee(request):
    template_name = 'employee/add_employee.html'

    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('employee:list_employees')
    else:
        form = EmployeeForm()

    context = {
        'form': form,
    }
    return render(request, template_name, context)