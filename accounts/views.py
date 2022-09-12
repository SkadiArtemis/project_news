from django.contrib.auth.models import User, Group
from django.views.generic.edit import CreateView
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from .models import BaseRegisterForm
from django.shortcuts import render


class BaseRegisterView(CreateView):
    model = User
    from_class = BaseRegisterForm
    success_url = '/'


@login_required
def upgrade_me(request):
    user = request.user
    authors_group = Group.objects.get(name='authors')
    if not request.user.groups.fillter(name='authors').exists():
        authors_group.user_set.add(user)
    return redirect('/')