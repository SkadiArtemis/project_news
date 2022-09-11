from .models import Author, Post, BaseRegisterForm
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from .forms import PostForm
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from django.shortcuts import redirect
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required


class AuthorListView(ListView):
    model = Author
    context_object_name = 'Authors'
    template_name = 'news/author_list.html'


class AuthorDetail(DetailView):
    model = Author
    context_object_name = 'author'
    template_name = 'news/author_detail.html'


class PostDetailView(DetailView):
    model = Post
    template_name = 'news.html'
    context_object_name = 'post'


class PostListView(DetailView):
    model = Post
    template_name = 'news.html'
    context_object_name = 'posts'


class PostCategory(CreateView):
    model = Post
    fields = ['__all__']


class ProductCreate(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'news_edit.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.quantity = 13
        return super().form_valid(form)


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'protect/index.html'


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

