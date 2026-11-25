from django.shortcuts import render, get_object_or_404, redirect
from .forms import PlanForm
from .models import Plan


def add_plan(request):
    template_name = 'plan/add_plan.html'
    context = {}
    if request.method == 'POST':
        form = PlanForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('plan:list_plans')
    else:
        form = PlanForm()
    context['form'] = form
    return render(request, template_name, context)


def list_plans(request):
    template_name = 'plan/list_plans.html'
    plans = Plan.objects.prefetch_related('modalities')
    context = {
        'plans': plans,
    }
    return render(request, template_name, context)


def edit_plan(request, id_plan):
    template_name = 'plan/add_plan.html'
    context = {}
    plan = get_object_or_404(Plan, id=id_plan)
    if request.method == 'POST':
        form = PlanForm(request.POST, instance=plan)
        if form.is_valid():
            form.save()
            return redirect('plan:list_plans')
    else:
        form = PlanForm(instance=plan)
    context['form'] = form
    return render(request, template_name, context)


def delete_plan(request, id_plan):
    plan = get_object_or_404(Plan, id=id_plan)
    plan.delete()
    return redirect('plan:list_plans')