from django.shortcuts import render
from .models import Employee


# Create your views here.
def list_employees(request):
    template_name = 'employee/list_employees.html'
    employees = Employee.objects.filter()
    context = {
        'employees': employees,
    }
    return render(request, template_name, context)