from django.views.generic import (ListView,
                                  DetailView,
                                  TemplateView,
                                  CreateView)
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import PostForm
from .models import Author, Post, Category


class AuthorListView(ListView):
    model = Author
    context_object_name = 'Authors'
    template_name = 'news/author_list.html'


class AuthorDetailView(DetailView):
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


class PostCategoryView(CreateView):
    model = Post
    fields = ['__all__']


class PostCreateView(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'news_edit.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.quantity = 13
        return super().form_valid(form)


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'protect/index.html'




