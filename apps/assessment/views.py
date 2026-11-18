from django.shortcuts import render, get_object_or_404, redirect
from .forms import AssessmentForm
from .models import Assessment

def list_assessments(request):
    template_name = 'assessment/assessment_list.html'
    assessments = Assessment.objects.all()
    context = {
        'assessments': assessments,
    }
    return render(request, template_name, context)

def add_assessment(request):
    template_name = 'assessment/assessment_form.html'
    context = {}
    if request.method == 'POST':
        form = AssessmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('assessment:assessment_list')
    form = AssessmentForm()
    context['form'] = form
    return render(request, template_name, context)