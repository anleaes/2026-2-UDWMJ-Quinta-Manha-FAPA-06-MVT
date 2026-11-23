from django.shortcuts import get_object_or_404, redirect ,render

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
def edit_person(request, id_person):
    template_name = 'person/add_person.html'
    person = get_object_or_404(Person, id=id_person)

    if request.method == 'POST':
        form = PersonForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return redirect('person:list_persons')
    else:
        form = PersonForm(instance=person)

    context = {
        'form': form,
        'person': person,
    }
    return render(request, template_name, context)
def delete_person(request, id_person):
    template_name = 'person/delete_person.html'
    person = get_object_or_404(Person, id=id_person)

    if request.method == 'POST':
        person.delete()
        return redirect('person:list_persons')

    context = {
        'person': person,
    }
    return render(request, template_name, context)