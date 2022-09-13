from django.urls import path
from .views import (
     PostListView,
     PostDetailView,
     AuthorListView,
     AuthorDetailView,
    )



urlpatterns = [
    path('authors/', AuthorListView.as_view()),
    path('authors/<int:pk>', AuthorDetailView.as_view()),
    path('news/', PostListView.as_view()),
    path('news/<int:pk>/', PostDetailView.as_view(), name='news_detail'),
    ]
