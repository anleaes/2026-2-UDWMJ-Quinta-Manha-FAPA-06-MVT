from django.shortcuts import redirect, render
from .models import Member
from .forms import MemberForm


# Create your views here.
def list_members(request):
    template_name = 'member/list_members.html'
    members = Member.objects.filter()
    context = {
        'members': members,
    }
    return render(request, template_name, context)
def add_member(request):
    template_name = 'member/add_member.html'

    if request.method == 'POST':
        form = MemberForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('member:list_members')
    else:
        form = MemberForm()

    context = {
        'form': form,
    }
    return render(request, template_name, context)