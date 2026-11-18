from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from .forms import AssessmentForm
from .models import Assessment

class AssessmentListView(ListView):
    model = Assessment
    template_name = 'assessment/assessment_list.html'
    context_object_name = 'assessments'