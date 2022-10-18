from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    AuthorListView,
    AuthorDetailView,
    subscribe_users,
)



urlpatterns = [
    path('authors/', AuthorListView.as_view()),
    path('authors/<int:pk>', AuthorDetailView.as_view()),
    path('news/', PostListView.as_view(), name='news-list'),
    path('news/<int:pk>/', PostDetailView.as_view(), name='news_detail'),
    path('subscribe/', subscribe_users, name='subscribe')
]
