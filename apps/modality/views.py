from django.shortcuts import render, get_object_or_404, redirect
from .forms import ModalityForm
from .models import Modality


def add_modality(request):
    template_name = 'modality/add_modality.html'
    context = {}
    if request.method == 'POST':
        form = ModalityForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('modality:list_modalities')
    else:
        form = ModalityForm()
    context['form'] = form
    return render(request, template_name, context)


def list_modalities(request):
    template_name = 'modality/list_modalities.html'
    modalities = Modality.objects.all()
    context = {
        'modalities': modalities,
    }
    return render(request, template_name, context)


def edit_modality(request, id_modality):
    template_name = 'modality/add_modality.html'
    context = {}
    modality = get_object_or_404(Modality, id=id_modality)
    if request.method == 'POST':
        form = ModalityForm(request.POST, request.FILES, instance=modality)
        if form.is_valid():
            form.save()
            return redirect('modality:list_modalities')
    else:
        form = ModalityForm(instance=modality)
    context['form'] = form
    return render(request, template_name, context)


def delete_modality(request, id_modality):
    modality = get_object_or_404(Modality, id=id_modality)
    modality.delete()
    return redirect('modality:list_modalities')