from django.shortcuts import render
from .models import Person

# Create your views here.
def list_persons(request):
    template_name = 'person/list_persons.html'
    persons = Person.objects.filter()
    context = {
        'persons': persons,
    }
    return render(request, template_name, context)