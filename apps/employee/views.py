from django.shortcuts import get_object_or_404, redirect, render
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
def edit_employee(request, id_employee):
    template_name = 'employee/add_employee.html'
    employee = get_object_or_404(Employee, id=id_employee)

    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employee:list_employees')
    else:
        form = EmployeeForm(instance=employee)

    context = {
        'form': form,
        'employee': employee,
    }
    return render(request, template_name, context)
def delete_employee(request, id_employee):
    template_name = 'employee/delete_employee.html'
    employee = get_object_or_404(Employee, id=id_employee)

    if request.method == 'POST':
        employee.delete(keep_parents=True)
        return redirect('employee:list_employees')

    context = {
        'employee': employee,
    }
    return render(request, template_name, context)