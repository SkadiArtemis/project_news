from django.contrib.auth.models import User, Group
from django.views.generic.edit import CreateView
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from .models import BaseRegisterForm
from django.shortcuts import render
from news_app1.views import Category
from news_app1.models import Post


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


def add_subscribe(request):
    pk = request.GET.get('pk')
    user = request.user
    subscribe_group = Group.objects.get(name='Subscribers')
    if not request.user.groups.fillter(name='Subscribers').exists():
        subscribe_group.user_set.add(user)
        Category.objects.get(pk=pk).subscribes.add(request.user)
    print(f'{request.user} подписался на новости {Category.objects.get(pk=pk)}')

    return redirect('/')


def subscribe_user(request):
    user = request.user
    print(user)
    category = Category.objects.get(id=request.Post['id_cat'])
    print(category)

    if category.subscribers.filter(id=user.id).exists():
        category.subscribers.remove(user)
    else:
        category.subscribers.add(user)

    return redirect('/profile')