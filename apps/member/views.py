from django.shortcuts import render
from .models import Member

# Create your views here.
def list_members(request):
    template_name = 'member/list_members.html'
    members = Member.objects.filter()
    context = {
        'members': members,
    }
    return render(request, template_name, context)