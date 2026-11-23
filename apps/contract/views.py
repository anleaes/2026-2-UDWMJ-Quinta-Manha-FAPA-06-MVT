from django.shortcuts import render, redirect, get_object_or_404
from .forms import ContractForm
from .models import Contract

# Create your views here.

def add_contract(request):
    template_name = 'contract/add_contract.html'
    context = {}
    if request.method == 'POST':
        form = ContractForm(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('contract:list_contracts')
    else:
        form = ContractForm()
    context['form'] = form
    return render(request, template_name, context)

def list_contracts(request):
    template_name = 'contract/list_contracts.html'
    contracts = Contract.objects.filter()
    context = {
        'contracts': contracts
    }
    return render(request, template_name, context)

def edit_contract(request, id_contract):
    template_name = 'contract/add_contract.html'
    context = {}
    contract = get_object_or_404(Contract, id=id_contract)
    if request.method == 'POST':
        form = ContractForm(request.POST, request.FILES, instance=contract)
        if form.is_valid():
            form.save()
            return redirect('contract:list_contracts')
    else:
        form = ContractForm(instance=contract)
    context['form'] = form
    return render(request, template_name, context)

def delete_contract(request, id_contract):
    contract = Contract.objects.get(id=id_contract)
    contract.delete()
    return redirect('contract:list_contracts')