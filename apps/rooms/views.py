
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST

from .forms import RoomForm
from .models import Room


def add_room(request):
    template_name = 'rooms/add_room.html'

    if request.method == 'POST':
        form = RoomForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('rooms:list_rooms')
    else:
        form = RoomForm()

    context = {'form': form}
    return render(request, template_name, context)


def list_rooms(request):
    template_name = 'rooms/list_rooms.html'
    rooms = Room.objects.all()

    context = {'rooms': rooms}
    return render(request, template_name, context)


def edit_room(request, id_room):
    template_name = 'rooms/add_room.html'
    room = get_object_or_404(Room, id=id_room)

    if request.method == 'POST':
        form = RoomForm(
            request.POST, request.FILES, instance=room
        )
        if form.is_valid():
            form.save()
            return redirect('rooms:list_rooms')
    else:
        form = RoomForm(instance=room)

    context = {'form': form}
    return render(request, template_name, context)


@require_POST
def delete_room(request, id_room):
    room = get_object_or_404(Room, id=id_room)
    room.delete()
    return redirect('rooms:list_rooms')
