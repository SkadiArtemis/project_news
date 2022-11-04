from urllib.request import Request
from django.views.generic import (ListView,
                                  DetailView,
                                  TemplateView,
                                  CreateView)
from django.http import HttpRequest
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import (Http404,
                         HttpResponse)
from django.urls import reverse
from django.shortcuts import redirect
from django.core.mail import EmailMultiAlternatives
from django.dispatch import receiver
from .forms import PostForm, SubscribeForm
from .models import (Author,
                     Post,
                     Subscribers,
                     Category)
from accounts.models import User
import logging

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

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            return redirect('search')

        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):

        user_id = request.user.id
        post_id = self.kwargs.get('pk')
        post_category = Post.objects.get(pk=post_id).postCategory.all()

        for item in post_category:
            cat_id = Category.objects.get(name__iexact=f'{item}').id
            subscriber = Subscribers(
                userID=user_id,
                categoryID=cat_id
            )
            subscriber.save()

            return redirect('/')


class PostListView(ListView):
    model = Post
    template_name = 'posts/list.html'
    context_object_name = 'posts'


class PostCategoryView(CreateView):
    model = Post
    fields = ['__all__']


class PostCreateView(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'news_edit.html'

    def form_valid(self, form):
        print(123)
        post = form.save(commit=False)
        post.quantity = 13
        return super().form_valid(form)


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'protect/index.html'


def subscribe_users(request: HttpRequest):
    if request.method == 'POST':
        form = SubscribeForm(request.POST)
        if form.is_valid():
            Subscribers.objects.create(
                user_id=request.user.id,
                category_id=form.data.get('category')[0],
            )
        url = reverse('news:news-list')
        return redirect(url)


logger = logging.getLogger('django')


def index(request):
    logger.error('Testing!')
    return HttpResponse('Hello this logging world!')