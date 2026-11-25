from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST

from .forms import ClassSessionForm
from .models import ClassSession


def add_class_session(request):
    template_name = 'class_sessions/add_class_session.html'

    if request.method == 'POST':
        form = ClassSessionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('class_sessions:list_class_sessions')
    else:
        form = ClassSessionForm()

    context = {'form': form}
    return render(request, template_name, context)


def list_class_sessions(request):
    template_name = 'class_sessions/list_class_sessions.html'
    class_sessions = ClassSession.objects.select_related(
        'modality', 'room', 'instructor'
    ).all()

    context = {'class_sessions': class_sessions}
    return render(request, template_name, context)


def edit_class_session(request, id_class_session):
    template_name = 'class_sessions/add_class_session.html'
    class_session = get_object_or_404(
        ClassSession, id=id_class_session
    )

    if request.method == 'POST':
        form = ClassSessionForm(
            request.POST, instance=class_session
        )
        if form.is_valid():
            form.save()
            return redirect('class_sessions:list_class_sessions')
    else:
        form = ClassSessionForm(instance=class_session)

    context = {'form': form}
    return render(request, template_name, context)


@require_POST
def delete_class_session(request, id_class_session):
    class_session = get_object_or_404(
        ClassSession, id=id_class_session
    )
    class_session.delete()
    return redirect('class_sessions:list_class_sessions')
