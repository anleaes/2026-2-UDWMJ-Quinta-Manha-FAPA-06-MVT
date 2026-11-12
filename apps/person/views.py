from django.shortcuts import redirect ,render

from .forms import PersonForm
from .models import Person

# Create your views here.
def list_persons(request):
    template_name = 'person/list_persons.html'
    persons = Person.objects.filter()
    context = {
        'persons': persons,
    }
    return render(request, template_name, context)
def add_person(request):
    template_name = 'person/add_person.html'

    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('person:list_persons')
    else:
        form = PersonForm()

    context = {
        'form': form,
    }
    return render(request, template_name, context)